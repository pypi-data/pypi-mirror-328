import os
import base64
import re
import argparse
import shutil
import json
import boto3
from dotenv import load_dotenv
from pdf2image import convert_from_path
from datetime import datetime

load_dotenv()

bedrock_client = boto3.client("bedrock-runtime", region_name="ap-south-1")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def convert_pdf_to_image(pdf_path, output_folder="temp"):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path, first_page=1, last_page=1)

    if not images:
        raise ValueError(f"No pages found in {pdf_path}")

    image_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".jpg"))
    images[0].save(image_path, "JPEG")
    return image_path

def extract_text_from_image(image_path):
    base64_image = encode_image(image_path)

    prompt = (
        "You are an extremely strict and efficient Invoice Details Extractor. "
        "You will receive an image of an invoice. Your task is to extract exactly three fields: "
        "1. 'Invoice No' - the exact invoice number as it appears; "
        "2. 'Invoice Dt' - the invoice date in the format DD.MM.YYYY (convert it if necessary); "
        "3. 'Supplier Name' - the supplier's name, which must never be 'Safari Exim House Pvt Ltd'.\n\n"
        "Follow these rules strictly:\n"
        "- Output only a JSON object with exactly three keys: 'Invoice No', 'Invoice Dt', and 'Supplier Name'.\n"
        "- Do not include any additional text, explanations, or keys.\n"
        "- If any required field is missing or uncertain, return an empty JSON object {}.\n"
        "Respond only with the JSON object without any markdown formatting or extra text."
    )

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": base64_image
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = bedrock_client.invoke_model(
            modelId="anthropic.claude-3-haiku-20240307-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload)
        )
        response_body = json.loads(response["body"].read())
        extracted_text = response_body["content"][0]["text"].strip()
        return extracted_text
    except Exception as e:
        print(f"Error processing: {str(e)}")
        return None

def extract_invoice_details(extracted_text):
    try:
        data = json.loads(extracted_text)
        required_keys = ["Invoice No", "Invoice Dt", "Supplier Name"]
        if not all(key in data for key in required_keys):
            print("⚠️ One or more required keys are missing in the JSON.")
            return {}
        return data
    except Exception as e:
        print(f"JSON parsing error: {str(e)}")
        return {}

def get_year_and_month(invoice_date):
    try:
        invoice_date = invoice_date.strip().replace('"', '').replace(',', '')
        date_obj = datetime.strptime(invoice_date, "%d.%m.%Y")
        return date_obj.year, date_obj.strftime("%B")
    except ValueError:
        return None, None

def sanitize_filename(filename):
    filename = filename.replace('"', '').replace(',', '')
    return re.sub(r'[^\w\s-]', '', filename).strip()

def process_subfolder(subfolder_path):
    pdf_files = [f for f in os.listdir(subfolder_path) if f.endswith(".pdf")]
    print(f"🔍 Processing {len(pdf_files)} PDFs in {subfolder_path}...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(subfolder_path, pdf_file)
        try:
            image_path = convert_pdf_to_image(pdf_path)
            print(f"Converted {pdf_file} to {image_path}")

            extracted_text = extract_text_from_image(image_path)
            print(f"Extracted Text from {pdf_file}:\n{extracted_text}\n")
            if not extracted_text:
                print(f"⚠️ No text extracted from {pdf_file}. Skipping.")
                continue

            invoice_details = extract_invoice_details(extracted_text)
            if not all(key in invoice_details for key in ["Invoice No", "Invoice Dt", "Supplier Name"]):
                print(f"⚠️ Missing required details from {pdf_file}. Skipping.")
                continue

            invoice_no = invoice_details["Invoice No"]
            invoice_dt = invoice_details["Invoice Dt"]
            supplier_name = invoice_details["Supplier Name"]

            formatted_invoice_no = invoice_no.replace("/", "-").replace('"', '').replace(',', '')
            formatted_supplier = sanitize_filename(supplier_name.replace(" ", ""))
            print(f"Extracted Invoice No: {formatted_invoice_no}")
            print(f"Extracted Invoice Dt: {invoice_dt}")
            print(f"Extracted Supplier Name: {formatted_supplier}\n")

            year, month = get_year_and_month(invoice_dt)
            if not year or not month:
                print(f"Invalid Invoice Dt. format for {pdf_file}. Skipping.")
                continue

            subfolder_name = os.path.basename(subfolder_path)
            output_parent_dir = os.path.join(subfolder_path, "Named")
            os.makedirs(output_parent_dir, exist_ok=True)

            output_dir = os.path.join(output_parent_dir, str(year), month)
            os.makedirs(output_dir, exist_ok=True)

            new_file_name = f"{formatted_invoice_no}-{formatted_supplier}.pdf"
            new_pdf_path = os.path.join(output_dir, new_file_name)
            shutil.copy(pdf_path, new_pdf_path)
            print(f"📂 Copied file to {new_pdf_path}")

            os.remove(image_path)
            print(f"🧹 Deleted temporary image: {image_path}")

        except Exception as e:
            print(f"Error processing {pdf_file}: {str(e)}")

def process_main_folder(main_folder):
    subfolders = [os.path.join(main_folder, f) for f in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, f))]
    
    if not subfolders:
        print("⚠️ No subfolders found inside the main input folder!")
        return

    for subfolder in subfolders:
        print(f"📂 Processing subfolder: {subfolder}")
        process_subfolder(subfolder)

def main():
    parser = argparse.ArgumentParser(
        description="Extract invoice details from PDFs and organize them."
    )
    parser.add_argument(
        "main_folder",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="Main folder containing subfolders with PDFs (default: current working directory)"
    )
    args = parser.parse_args()
    process_main_folder(args.main_folder)

if __name__ == "__main__":
    main()

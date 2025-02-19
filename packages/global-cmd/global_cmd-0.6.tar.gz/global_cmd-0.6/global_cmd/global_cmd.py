import os
import base64
import re
import argparse
import shutil
from openai import OpenAI
from dotenv import load_dotenv
from pdf2image import convert_from_path
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("openaiprem"))

if not client.api_key:
    raise ValueError(" OpenAI API key is missing. Ensure .env contains 'openaiprem'.")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def convert_pdf_to_image(pdf_path, output_folder="temp"):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path, first_page=1, last_page=1)

    if not images:
        raise ValueError(f" No pages found in {pdf_path}")

    image_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".jpg"))
    images[0].save(image_path, "JPEG")
    return image_path

def extract_text_from_image(image_path):
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "You are an Image details extractor expert. Extract only the Invoice No, Invoice Dt., and Supplier Name from this image. Ensure you do not extract anything else. Also, the Supplier Name will never be 'Safari Exim House Pvt Ltd.' Display the details in JSON format."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        ],
    )
    print("📡 OpenAI API Response:", response)
    extracted_text = response.choices[0].message.content.strip()
    return extracted_text


def extract_invoice_details(extracted_text):
    details = extracted_text.split("\n")
    invoice_details = {}

    for line in details:
        if "Invoice No" in line:
            invoice_details["invoice_no"] = line.split(":")[-1].strip()
        elif "Invoice Dt" in line or "Invoice Date" in line:
            invoice_details["invoice_dt"] = line.split(":")[-1].strip()
        elif "Supplier Name" in line:
            invoice_details["supplier_name"] = line.split(":")[-1].strip()

    return invoice_details


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


def process_pdfs(pdf_folder):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    print(f"🔍 Processing {len(pdf_files)} PDFs in {pdf_folder}...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)

        try:
            image_path = convert_pdf_to_image(pdf_path)
            print(f"Converted {pdf_file} to {image_path}")

            extracted_text = extract_text_from_image(image_path)
            print(f" Extracted Text from {pdf_file}:\n{extracted_text}\n")

            invoice_details = extract_invoice_details(extracted_text)

            if not all(key in invoice_details for key in ["invoice_no", "invoice_dt", "supplier_name"]):
                print(f"⚠️ Missing required details from {pdf_file}. Skipping.")
                continue

            invoice_no = invoice_details["invoice_no"]
            invoice_dt = invoice_details["invoice_dt"]
            supplier_name = invoice_details["supplier_name"]
            formatted_invoice_no = invoice_no.replace("/", "-")
            formatted_invoice_no = formatted_invoice_no.replace('"', '')
            formatted_invoice_no = formatted_invoice_no.replace(',', '')

            formatted_supplier = sanitize_filename(supplier_name.replace(" ", ""))
            print(f" Extracted Invoice No: {formatted_invoice_no}")
            print(f" Extracted Invoice Dt: {invoice_dt}")
            print(f" Extracted Supplier Name: {formatted_supplier}\n")

            year, month = get_year_and_month(invoice_dt)
            if not year or not month:
                print(f" Invalid Invoice Dt. format for {pdf_file}. Skipping.")
                continue
            parent_dir = "Structure"
            os.makedirs(parent_dir, exist_ok=True)
            output_dir = os.path.join(parent_dir, str(year), month)
            os.makedirs(output_dir, exist_ok=True)
            new_file_name = f"{formatted_invoice_no}-{formatted_supplier}.pdf"
            new_pdf_path = os.path.join(output_dir, new_file_name)

            shutil.copy(pdf_path, new_pdf_path)
            print(f"📂 Copied file to {new_pdf_path}")

            os.remove(image_path)
            print(f"🧹 Deleted temporary image: {image_path}")

        except Exception as e:
            print(f" Error processing {pdf_file}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Extract invoice details from PDFs and organize them.")
    parser.add_argument("pdf_folder", type=str, nargs="?", default=os.getcwd(), help="Folder containing PDFs (default: current working directory)")
    args = parser.parse_args()
    process_pdfs(args.pdf_folder)

if __name__ == "__main__":
    main()

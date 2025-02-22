# setup.py
from setuptools import setup, find_packages

setup(
    name="global_cmd",
    version="1.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "pdf2image",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "global_cmd=global_cmd.global_cmd:main",  
        ],
    },
)

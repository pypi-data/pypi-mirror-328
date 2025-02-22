from setuptools import setup, find_packages

setup(
    name="ocr_json_processor",
    version="0.5.0",
    description="A package for OCR response and JSON updates.",
    author="Shubham Kumar",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "numpy",
        "python-dotenv",
        "azure-core",
        "azure-ai-documentintelligence==1.0.0b2",
        "amazon-textract-textractor==1.7.10",
        "PyMuPDF",
        "pytest",
        "fastapi",
        "fuzzywuzzy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdfgenius",
    version="0.1.3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(
        include=["pdfgenius", "pdfgenius.*"]
    ),  # Explicitly include packages
    install_requires=[
        "pdf2image",
        "Pillow",
        "python-dotenv",
        "click",
        "google-genai",
        "openai",
        "cryptography",
    ],
    entry_points={
        "console_scripts": [
            "pdfgenius=pdfgenius.cli:main",
        ],
    },
    python_requires=">=3.7",
)

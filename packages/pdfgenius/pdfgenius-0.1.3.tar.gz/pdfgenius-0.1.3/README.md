# PDF GENIUS

PDF GENUIS is a powerful Python package that converts PDF documents into text using AI-powered optical character recognition (OCR). It currently supports both Google's Gemini and OpenAI's GPT-4 Vision models for text extraction, with an extensible architecture that makes it easy to add support for additional AI models.

## Features

- Extract text from PDF documents using state-of-the-art AI models
- Support for multiple AI providers (Gemini and OpenAI)
- Secure local storage of API keys
- Command-line interface (CLI) for easy use
- Extensible architecture for adding new AI models
- Automatic handling of multi-page PDFs
- Clean temporary file management

## Installation

You can install the package using pip:

```bash
pip install pdfgenius
```

The package requires Python 3.7 or later.

### System Dependencies

This package requires Poppler for PDF processing. Install it based on your operating system:

- **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt-get install poppler-utils
  ```

- **macOS**:

  ```bash
  brew install poppler
  ```

- **Windows**:
  Download and install poppler from [poppler releases](http://blog.alivate.com.au/poppler-windows/), then add the bin directory to your system PATH.

## Quick Start

Extract text from a PDF using the default Gemini model:

```bash
# Store your API key (one-time setup)
pdfgenius keys add gemini "your-gemini-api-key"

# Extract text from PDF
pdfgenius extract document.pdf
```

## API Key Management

The package provides secure local storage for your API keys. You can manage them using these commands:

```bash
# Add an API key
pdfgenius keys add gemini "your-gemini-api-key"
pdfgenius keys add openai "your-openai-api-key"

# List stored keys (shows partial keys for security)
pdfgenius keys list

# Delete a stored key
pdfgenius keys delete gemini
```

## Command Line Usage

### Basic Usage

```bash
# Extract using default settings (Gemini model)
pdfgenius extract document.pdf

# Specify output file
pdfgenius extract document.pdf -o output.txt

# Use OpenAI model
pdfgenius extract document.pdf -m openai

# Provide API key directly (without storing)
pdfgenius extract document.pdf -m openai --api-key "your-api-key"
```

### Full Command Reference

```bash
# Show help
pdfgenius --help

# Show help for extract command
pdfgenius extract --help

# Show help for key management
pdfgenius keys --help
```

## Python API

You can also use the package programmatically in your Python code:

```python
from pdf_extractor import GeminiExtractor, OpenAIExtractor
from pdf_extractor.utils import process_pdf

# Using Gemini
extractor = GeminiExtractor(api_key="your-api-key")
extractor.initialize_client()
text = process_pdf("document.pdf", extractor)

# Using OpenAI
extractor = OpenAIExtractor(api_key="your-api-key")
extractor.initialize_client()
text = process_pdf("document.pdf", extractor)
```

## Adding Support for New AI Models

The package is designed to be easily extensible. To add support for a new AI model:

1. Create a new extractor class that inherits from `BaseExtractor`
2. Implement the required methods
3. Register the new extractor in the CLI

Example:

```python
from pdf_extractor.extractors.base import BaseExtractor

class NewModelExtractor(BaseExtractor):
    def initialize_client(self):
        # Initialize your AI client
        pass

    def extract_text_from_image(self, image_path: Path) -> str:
        # Implement text extraction logic
        pass
```

## Security

- API keys are stored encrypted in the user's home directory
- The encryption key is stored separately
- Only partial keys are displayed when listing stored keys
- Keys can be easily deleted when no longer needed

## Environment Variables

The package also supports providing API keys through environment variables:

```bash
export GEMINI_API_KEY="your-gemini-api-key"
export OPENAI_API_KEY="your-openai-api-key"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This package uses several open-source libraries:

- pdf2image for PDF processing
- google-generativeai for Gemini API
- openai for OpenAI API
- click for CLI interface
- cryptography for secure key storage

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

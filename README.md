# Document Converter

This project is a simple yet powerful document conversion tool that can convert between different file formats. Currently, it supports the following conversions:

- Markdown (.md) to PDF
- PDF to Text
- Word (.docx) to Text

## Features

- Convert Markdown files to well-formatted PDFs
- Extract text from PDF files
- Extract text from Word documents
- Batch processing of multiple files
- Detailed logging for tracking conversion progress and errors

## Requirements

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory:

   ```
   cd path/to/document-converter
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Project Structure

```
document-converter/
├── main.py
├── document_converter.py
├── tools/
│   ├── __init__.py
│   ├── markdown_to_pdf.py
│   ├── pdf_to_txt.py
│   └── word_to_txt.py
├── source_files/
├── converted_files/
├── requirements.txt
└── README.md
```

## Usage

1. Place the files you want to convert in the `source_files` directory.

2. Run the conversion script:

   ```
   python main.py
   ```

3. The converted files will be saved in the `converted_files` directory.

## Supported File Types

- Input:
  - Markdown (.md)
  - PDF (.pdf)
  - Word (.docx)

- Output:
  - PDF (from Markdown)
  - Text (from PDF and Word)

## Logging

The script provides detailed logging information. You can find:
- Conversion progress for each file
- Any errors encountered during the conversion process
- A summary of the total number of files converted

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed.
2. Check that your input files are not corrupted and are in the correct format.
3. Verify that you have write permissions in the `converted_files` directory.
4. Check the console output for any error messages.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



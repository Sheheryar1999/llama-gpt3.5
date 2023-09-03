import os
import PyPDF2
import json

def pdf_to_txt(input_pdf_file, output_dir=None):
    try:
        # Open the input PDF file in read-binary mode
        with open(input_pdf_file, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty string to store text
            text = ""

            # Loop through each page and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Generate the output TXT file name based on the input file name
            if output_dir is None:
                output_dir = os.path.dirname(input_pdf_file)
            output_txt_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_pdf_file))[0] + '.txt')

            # Write the extracted text to the output TXT file
            with open(output_txt_file, 'w', encoding='utf-8') as txt_output:
                txt_output.write(text)

        print(f"PDF converted to TXT: {output_txt_file}")
        return output_txt_file
    except Exception as e:
        print(f"Error converting PDF to TXT: {e}")
        return None

def json_to_txt(input_json_file, output_dir=None):
    try:
        # Read the input JSON file
        with open(input_json_file, 'r', encoding='utf-8') as json_input:
            data = json.load(json_input)

        # Convert the JSON data to a formatted string
        text = json.dumps(data, indent=4)

        # Generate the output TXT file name based on the input file name
        if output_dir is None:
            output_dir = os.path.dirname(input_json_file)
        output_txt_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_json_file))[0] + '.txt')

        # Write the formatted JSON text to the output TXT file
        with open(output_txt_file, 'w', encoding='utf-8') as txt_output:
            txt_output.write(text)

        print(f"JSON converted to TXT: {output_txt_file}")
        return output_txt_file
    except Exception as e:
        print(f"Error converting JSON to TXT: {e}")
        return None

import PyPDF2
import re


def extract_formulas_from_pdf(pdf_path):
    formulas = set()  # Use a set to store unique formulas

    pdf_reader = PyPDF2.PdfReader(pdf_path)

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        # Use regex to find and extract formulas within <formula> tags
        formula_matches = re.findall(r'<formula>(.*?)<\/formula>', page_text, re.DOTALL)
        formulas.update(formula_matches)  # Add unique formulas to the set

    return list(formulas)  # Convert set to list before returning


def save_formulas_to_txt(formulas, output_file):
    # Read existing formulas from the text file, if any
    existing_formulas = set()
    try:
        with open(output_file, 'r', encoding='utf-8') as file:
            for line in file:
                existing_formulas.add(line.strip())
    except FileNotFoundError:
        pass  # File doesn't exist yet, ignore the exception

    # Find new, unique formulas
    new_formulas = [formula for formula in formulas if formula not in existing_formulas]

    # Append new, unique formulas to the text file
    with open(output_file, 'a', encoding='utf-8') as file:
        for formula in new_formulas:
            file.write(formula.strip() + '\n')

def remove_duplicate_lines(input_file, output_file):
    unique_lines = set()

    # Read the input file and store unique lines in the set
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            unique_lines.add(line.strip())

    # Write the unique lines back to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in unique_lines:
            outfile.write(line + '\n')

def main():
    pdf_path = ('./training_data/text3.pdf')
    output_file = 'eq_dir/extracted_formulas.txt'

    extracted_formulas = extract_formulas_from_pdf(pdf_path)

    if extracted_formulas:
        save_formulas_to_txt(extracted_formulas, output_file)
        print(f"Formulas extracted and saved to {output_file}")
        remove_duplicate_lines('eq_dir/extracted_formulas.txt', 'eq_dir/extracted_formulas.txt')

    else:
        print("No formulas found in the PDF.")


if __name__ == "__main__":
    main()

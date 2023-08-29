import re
import fitz

#JGVVLW-EXQ2PQA7J2
def extract_formulas_with_labels(text_and_layouts):
    formula_start = "<formula>"
    formula_end = "</formula>"
    formulas = []

    for text, layout in text_and_layouts:
        start_positions = [m.start() for m in re.finditer(re.escape(formula_start), text)]
        end_positions = [m.start() for m in re.finditer(re.escape(formula_end), text)]

        for start_pos, end_pos in zip(start_positions, end_positions):
            formula = text[start_pos + len(formula_start):end_pos].strip()

            #replace the goofy multiplication sign
            formula = formula.replace("×", "*")
            formula = formula.replace('≥', '>=')

            # Check if the formula is not already in the list
            if formula not in formulas:
                formulas.append(formula)

    output_file = "data/formulas.txt"
    with open(output_file, "w") as file:
        for idx, formula in enumerate(formulas, 1):
            file.write(f"{formula}\n")

    print("Formulas saved to", output_file)
    return formulas

def extract_text_and_layout(pdf_path):
    doc = fitz.open(pdf_path)
    pages = doc.page_count
    text_and_layouts = []

    for page_number in range(pages):
        page = doc[page_number]
        text = page.get_text("text")
        layout = page.get_displaylist()
        text_and_layouts.append((text, layout))

    doc.close()
    return text_and_layouts



# Example usage with formulas:
pdf_path = "/home/blnk/Documents/LLAMA_IND/test_digest/test.pdf"
text_and_layouts = extract_text_and_layout(pdf_path)
formulas_with_labels = extract_formulas_with_labels(text_and_layouts)
for idx, formula in enumerate(formulas_with_labels, 1):
    print(f"Formula {idx}: {formula}")

##Example just layout
# pdf_path = "/home/blnk/Documents/LLAMA_IND/test_digest/test1.pdf"
# text_and_layouts = extract_text_and_layout(pdf_path)
# for page_number, (text, layout) in enumerate(text_and_layouts, 1):
#     print(f"Page {page_number} Text: {text[:100]}...")
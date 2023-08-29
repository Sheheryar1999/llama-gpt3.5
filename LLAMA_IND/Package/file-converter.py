from common import *


def pdf_to_text(pdf_var, txt_var):
    with open(pdf_var, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        with open(txt_var, 'w') as txt_file:
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                txt_file.write(text)


def json_to_txt(json_path, txt_path):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
        with open(txt_path, 'w') as txt_file:
            txt_file.write(json.dumps(data, indent=4))



# pdf_to_text('text2.pdf', './Actual/example2.txt')
# pdf_to_text('./Actual/text.pdf', './Actual/example.txt')
# json_to_txt('example.json', 'example.txt')

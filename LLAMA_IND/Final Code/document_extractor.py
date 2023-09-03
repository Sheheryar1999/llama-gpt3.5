from converter import pdf_to_txt, json_to_txt

# usage
# pdf_to_txt('input.pdf', my directory)
# json_to_txt('input.json', my directory)


input_type = input("Enter Document type: ")


if(input_type == "pdf"):
    path= input("Enter Document path")
    pdf_to_txt(path, "data")

if (input_type == "json"):
    path = input("Enter Document path")
    json_to_txt(path, "data")

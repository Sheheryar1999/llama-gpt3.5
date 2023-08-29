def check_for_duplicates(formulas):
    unique_formulas = set()
    duplicates = []

    for formula in formulas:
        if formula in unique_formulas:
            duplicates.append(formula)
        else:
            unique_formulas.add(formula)

    return duplicates

def keep_unique_formulas(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        formulas = file.readlines()

    unique_formulas = set()
    unique_formulas_order_preserved = []

    for formula in formulas:
        if formula not in unique_formulas:
            unique_formulas.add(formula)
            unique_formulas_order_preserved.append(formula)

    with open(output_filename, 'w') as file:
        file.writelines(unique_formulas_order_preserved)

def main():
    input_filename = 'data/formulas.txt'
    output_filename = 'data/unique_formulas.txt'

    with open(input_filename, 'r') as file:
        formulas = file.readlines()

    duplicates = check_for_duplicates(formulas)

    if duplicates:
        print("Duplicate formulas found:")
        for duplicate in duplicates:
            print(duplicate)
    else:
        print("No duplicate formulas found.")

    keep_unique_formulas(input_filename, output_filename)
    print(f"Unique formulas have been saved to {output_filename}")

if __name__ == "__main__":
    main()

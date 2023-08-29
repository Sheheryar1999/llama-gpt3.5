import re
import sympy as sp

def extract_parameters(formula_str):
    # Extract parameters after the >= symbol
    parameters = re.findall(r'(\w+)\s*\*', formula_str)
    return parameters

def preprocess_formula(formula_str):
    formula_str = formula_str.replace('≥', '>=')
    formula_str = formula_str.replace('^', '**')
    return formula_str

def main():
    # Read formulas from the text file
    with open('data/formulas.txt', 'r') as file:
        formulas = file.readlines()

    # Display available formulas
    for idx, formula in enumerate(formulas, start=1):
        print(f"{idx}: {formula.strip()}")

    # Prompt user to select a formula
    selected_idx = int(input("Select a formula (1, 2, 3, etc.): ")) - 1
    selected_formula_str = formulas[selected_idx]

    # Preprocess the selected formula
    selected_formula_str = preprocess_formula(selected_formula_str)

    # Extract parameters from the formula
    parameters = extract_parameters(selected_formula_str)

    # Define symbolic variables
    symbolic_vars = sp.symbols(parameters)

    # Prompt user for parameter values
    param_values = {}
    for param in parameters:
        value = float(input(f"Enter value for parameter '{param}': "))
        param_values[param] = value

    # Parse and simplify the formula
    selected_formula = sp.sympify(selected_formula_str)

    # Solve the inequality for n
    n = sp.symbols('n')
    solution = sp.solve(selected_formula, n)

    print("Solution for n:", solution)

if __name__ == "__main__":
    main()

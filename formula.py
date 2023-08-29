import re
import sympy as sp
#Using another method api
#sympy api
def extract_parameters(formula_str):
    # Extract parameters after the >= symbol
    parameters = re.findall(r'(\w+)\s*\*', formula_str)
    return parameters

def preprocess_formula(formula_str):
    formula_str = formula_str.replace('≥', '>=')
    formula_str = formula_str.replace('^', '**')
    return formula_str

def main():
    with open('data/formulas.txt', 'r') as file:
        formulas = file.readlines()

    for idx, formula in enumerate(formulas, start=1):
        print(f"{idx}: {formula.strip()}")

    selected_idx = int(input("Select a formula: ")) - 1
    selected_formula = formulas[selected_idx]

    selected_formula = preprocess_formula(selected_formula)
    parameters = extract_parameters(selected_formula)

   # symbolic_vars = sp.symbols(parameters)

    # Prompt user for parameter values
    param_values = {}
    for param in parameters:
        value = float(input(f"Enter value for parameter '{param}': "))
        param_values[param] = value

    # Parse and simplify the formula
    formula = sp.sympify(selected_formula)

    # Solve for n
    n = sp.symbols('n')
    solution = sp.solve_univariate_inequality(formula, n)

    print("Solution for n:", solution)

if __name__ == "__main__":
    main()

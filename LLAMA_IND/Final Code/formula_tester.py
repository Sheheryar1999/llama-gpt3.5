import re
import math

# Function to extract variables from a formula
def extract_variables(formula):
    # Use regular expressions to find variable names (strings of letters and possibly digits)
    variables = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', formula)
    return variables

# Dictionary of available formulas
formulas = {
    "Formula 1": "n ≥ (m×g)/(2× sin(α)× Ft)× (Cy×h/w-Cz)×fs",
    "Formula 2": "n ≥ (m×g)/(2× sin( α)× Ft)× (Cx×h/w-Cz)×fs",
    "Formula 3": "n ≥ ((Cxy - μ × Cz)×m×g)/(2 × μ × sin(α)× Ft)× fs",
    "Formula 4": "n ≥ (m×g× (Cx×h-Cz×1))/(2× sin(α) × Ft×1)×fs"
}

# Display available formulas to the user
print("Available Formulas:")
for i, formula_name in enumerate(formulas.keys(), start=1):
    print(f"{i}. {formula_name}")

# Ask the user to choose a formula
while True:
    try:
        choice = int(input("Choose a formula (enter the number): "))
        if 1 <= choice <= len(formulas):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

selected_formula_name = list(formulas.keys())[choice - 1]
selected_formula = formulas[selected_formula_name]

# Extract variables from the selected formula
variables = extract_variables(selected_formula)

# Prompt the user to enter values for each variable on the right-hand side of the formula
variable_values = {}
print(f"Variables in {selected_formula_name}: {variables}")
for variable in variables:
    if variable == 'α':
        # Ask for the value of α (alpha) in degrees and convert it to radians
        alpha_degrees = float(input(f"Enter the value of α (alpha) in degrees: "))
        alpha_radians = math.radians(alpha_degrees)
        variable_values[variable] = alpha_radians
    else:
        value = float(input(f"Enter the value for {variable}: "))
        variable_values[variable] = value

# Display the entered variable values
print("Entered variable values:")
for variable, value in variable_values.items():
    print(f"{variable}: {value}")

# Calculate the result of the formula
result = eval(selected_formula, variable_values)
print(f"Result of the formula: {result}")

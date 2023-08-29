import re
import requests
#Using wolfram api
# Define a mapping of trigonometric functions to their mathematical expressions
TRIG_FUNCTIONS = {
    "sin": "sin({})", "cos": "cos({})", "tan": "tan({})",
    "asin": "asin({})", "acos": "acos({})", "atan": "atan({})"
}

def evaluate_formula_with_parameters(formula, parameters, api_key):
    formula = replace_trig_functions(formula)
    expression = formula.format(**parameters)

    base_url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": expression,
        "format": "plaintext",
        "output": "JSON",
        "appid": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["queryresult"]["success"]:
        pods = data["queryresult"]["pods"]
        for pod in pods:
            if pod["title"] == "Result":
                return pod["subpods"][0]["plaintext"]
    else:
        return "Error: Unable to evaluate formula"

def replace_trig_functions(formula):
    # Replace trigonometric function names with maths version
    for func, expr in TRIG_FUNCTIONS.items():
        formula = formula.replace(func, expr.format(func))
    return formula

def main():
    api_key = "JGVVLW-EXQ2PQA7J2"

    with open("data/formulas.txt", "r") as file:
        formulas = file.readlines()

    print("Available Formulas:")
    for idx, formula in enumerate(formulas, 1):
        print(f"{idx}: {formula.strip()}")

    try:
        formula_index = int(input("Select a formula (enter the corresponding index): ")) - 1
        selected_formula = formulas[formula_index].strip()

        # Prompt the user for input parameters
        parameters = {}
        for param in re.findall(r"\b[a-zA-Z_]\w*\b", selected_formula):
            value = float(input(f"Enter the value for '{param}': "))
            parameters[param] = value

        result = evaluate_formula_with_parameters(selected_formula, parameters, api_key)
        print(f"Result of the formula '{selected_formula}': {result}")

    except (ValueError, IndexError) as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

from langchain.llms import OpenAI
from langchain.chains.llm_symbolic_math.base import LLMSymbolicMathChain
import keys
keys.key_setting()
# Initialize LLMSymbolicMathChain
llm = OpenAI(temperature=0)
llm_symbolic_math = LLMSymbolicMathChain.from_llm(llm)

# Read formulas from the text file
with open('data/extracted_formulas.txt', 'r') as file:
    formulas = file.readlines()

# Display the available formulas to the user
for i, formula in enumerate(formulas):
    print(f'{i+1}. {formula.strip()}')

# Prompt the user to choose a formula
selected_formula_index = int(input('Which one?: ')) - 1
selected_formula = formulas[selected_formula_index]

def extract_variables(formula):
    # Initialize LLMSymbolicMathChain
    llm = OpenAI(temperature=0)
    llm_symbolic_math = LLMSymbolicMathChain.from_llm(llm)

    # Extract variables from the formula
    variables = llm_symbolic_math.extract_variables(formula)

    return variables
# Prompt the user for parameter values
parameter_values = {}
for parameter in llm_symbolic_math.extract_variables(selected_formula):
    value = input(f'Enter the value for parameter {parameter}: ')
    parameter_values[parameter] = value

# Replace parameter placeholders in the formula with the provided values
for parameter, value in parameter_values.items():
    selected_formula = selected_formula.replace(parameter, value)

# Run the formula through LLMSymbolicMathChain
result = llm_symbolic_math.run(selected_formula)

# Display the result
print(f'The result of the formula "{selected_formula}" is: {result}')
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
import keys
keys.key_setting()
import math

def display_text_file_contents(file_path):
    try:
        with open(file_path, "r", encoding= "utf-8") as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


file_path = 'eq_dir/extracted_formulas.txt'
def save_parameters_to_file(file_path, parameters):
       with open(file_path, 'w') as file:
           for parameter, value in parameters.items():
               file.write(f"{parameter} = {value}\n")
       print(f"Parameters saved to '{file_path}'.")

def prompt_user_for_parameters(parameters):
    user_values = {}
    for parameter in parameters.items():
        user_input = input(f"Enter the value for {parameter}: ")
        try:
            value = float(user_input)
            user_values[parameter] = value
        except ValueError:
            print(f"Invalid input. Please enter a valid numeric value for {parameter}.")

    return user_values

path = "eq_dir/extracted_formulas.txt"
# save_path_var = "variables.txt"
documents = SimpleDirectoryReader('./eq_dir').load_data()
index = GPTVectorStoreIndex(documents)

# display_formulas(path)
display_text_file_contents(path)

user_input = input("Enter Number: ")
query = f"Give me a comma separated list of variables required in formula {user_input}, excluding the left hand side variables"
engine = index.as_query_engine()
response = engine.query(query)

# print(type(response))

values = response.response

# print(type(response))
# print( type(values))
print(values)

parameter_names = values.split(", ")
parameter_values = {}

for parameter in parameter_names:
    while True:
        value = input(f"Please provide the value of {parameter}: ")
        if value.strip() == "":
            print("No value provided. Try again.")
        elif(value.strip() == "α"):
            val_deg = float(value)
            value = math.radians(val_deg)
        else:
            parameter_values[parameter] = value
            break

# Print the gathered parameter values
print("Gathered Parameter Values:")
for parameter, value in parameter_values.items():
    print(f"{parameter}: {value}")

query = f" for formula {user_input}, using the values {parameter_values} to calculate the value, show your working"
engine = index.as_query_engine()
response = engine.query(query)
print(response)
import keys
keys.key_setting()
import openai
import json

messages = [
    {"role": "system", "content": "You're an assistant that gives short and concise answers"}
]

#
# def save_chat_history(self, filename):
#     with open(filename, 'w') as f:
#         json.dump(self.chat_history, f)
#
#
# def load_chat_history(self, filename):
#     try:
#         with open(filename, 'r') as f:
#             self.chat_history = json.load(f)
#     except FileNotFoundError:
#         pass
#
while True:
    query = input("Enter Query: ")
    if(query == 'quit'):
        print("Goodbye")
        break

    messages.append({"role": "user", "content": query})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})
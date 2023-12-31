import json
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
import keys
keys.key_setting()

class Chatbot:
    def __init__(self, index):
        self.index = index
        self.chat_history = []

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}" for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}. Answer in Spanish"


        engine = index.as_query_engine()
        response = engine.query(user_input)

        message = ({"role": "assistant", "content": response.response})
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message

    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f, indent=4)




documents = SimpleDirectoryReader('data/text/').load_data()
index = GPTVectorStoreIndex(documents)


bot = Chatbot(index=index)
bot.load_chat_history("chat_history.json")


while True:
    user_input = input("Enter Query: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Bot: Goodbye!")
        bot.save_chat_history("chat_history.json")
        break
    response = bot.generate_response(user_input)
    print(f"Bot: {response['content']}")

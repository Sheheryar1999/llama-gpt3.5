from chat_class import *

bot = Chatbot("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", index=index)
bot.load_chat_history("chat_history.json")

user_input = input("You: ")
if user_input.lower() in ["bye", "goodbye"]:
    print("Bot: Goodbye!")
    bot.save_chat_history("chat_history.json")

response = bot.generate_response(user_input)
print(f"Bot: {response['content']}")

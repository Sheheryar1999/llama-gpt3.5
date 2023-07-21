import openai

API_KEY = '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'

openai.api_key = API_KEY


model_id = 'gpt-3.5-turbo'

def demo_chat(chat):
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = chat
    )

    # api_usage = response['usage']
    # print('Tokens used: {0}'.format(api_usage['total_tokens']))

    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)

    chat.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return chat

chat = []
chat.append({'role': 'system', 'content': 'How can you help me?'})

response = openai.ChatCompletion.create(
    model = model_id,
    messages = chat
)

print(response)

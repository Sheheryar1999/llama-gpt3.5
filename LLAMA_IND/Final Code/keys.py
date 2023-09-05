import openai
import os

key_id=""

def key_setting():
    os.environ['OPENAI_API_KEY'] = key_id
    openai.api_key =key_id

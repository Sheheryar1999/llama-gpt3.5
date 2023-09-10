import openai
import os
from dotenv import load_dotenv

load_dotenv()

key_id = os.getenv("OPENAI_API_KEY")


def key_setting():
    os.environ['OPENAI_API_KEY'] = key_id
    openai.api_key = key_id

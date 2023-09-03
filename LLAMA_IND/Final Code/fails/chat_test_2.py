from llama_index import  SimpleDirectoryReader, GPTVectorStoreIndex, readers, GPTListIndex, LLMPredictor, PromptHelper, ServiceContext
import keys
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
keys.key_setting()
import sys
from IPython.display import Markdown, display


def build_index(path):
    max_input_size = 4096
    num_outputs = 2000
    max_chunk_overlap = 0
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    index.save_to_disk('index.json')
    return index


def chat_function():
    index = GPTVectorStoreIndex.load_from_disk('index.json')
    while True:
        query = input("What do you want to ask? ")
        response = index.query(query)
        display(Markdown(f"Response: <b>{response.response}</b>"))


build_index("../data")
chat_function()
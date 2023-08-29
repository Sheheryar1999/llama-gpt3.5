from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from llama_index import LLMPredictor, PromptHelper
from llama_index import download_loader
import openai
import json
import PyPDF2
import os
os.environ['OPENAI_API_KEY'] = "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"
openai.api_key ="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"
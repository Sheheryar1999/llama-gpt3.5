from common import  *


openai.api_key ="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"
documents = SimpleDirectoryReader('./data').load_data()
index = GPTVectorStoreIndex(documents)
engine = index.as_query_engine()
response = engine.query("What is LLama?")
print(response)

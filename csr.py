from common import  *


docs = SimpleDirectoryReader('./data').load_data()
index = GPTVectorStoreIndex(docs)
engine = index.as_query_engine()
response = engine.query("How do I train chatgpt with my own data")
print(response)
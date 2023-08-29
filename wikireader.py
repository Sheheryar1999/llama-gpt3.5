from common import *

wikireader = download_loader('WikipediaReader')

loader = wikireader()


# https://en.wikipedia.org/wiki/Yinchuan

wikidocs = loader.load_data(pages=['Yinchuan'])

wiki_index = GPTVectorStoreIndex(wikidocs)

engine = index.as_query_engine()
response = engine.query("Where is Yinchuan?")
print(response)
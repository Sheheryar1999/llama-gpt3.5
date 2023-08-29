from llama_index import download_loader
from llama_index import GPTVectorStoreIndex
import openai
import os

os.environ["OPENAI_API_KEY"] = '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'

openai.api_key ='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'


YTtranscriptreader = download_loader("YoutubeTranscriptReader")
loader = YTtranscriptreader()

ytlinks=[]

lang = ['en', 'es','sp']

def create_query():

    x = input("Enter Video Link: \n")
    ytlinks.append(x)


def get_response():
    psu = loader.load_data(ytlinks, lang)
    index = GPTVectorStoreIndex(psu)
    engine = index.as_query_engine()
    query = input("Enter Query: ")
    response = engine.query(query)
    print(response)


create_query()
get_response()
ch = input("Would you like to ask another query?")
if (ch=='Y'):
    create_query()
    get_response()


print("Thanks")

##Que es Aglae Ekosystem

##https://www.youtube.com/watch?v=vgbMR0lDQBI  STEP2

##https://www.youtube.com/watch?v=TwipifOVZUw   STEP1
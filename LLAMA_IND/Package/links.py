from youtube_transcript_api import YouTubeTranscriptApi
from common import  *
openai.api_key ="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"

def create_link_text(id):
    outl = []
    lang = ['en', 'es','sp']
    text = YouTubeTranscriptApi.get_transcript(id, lang)

    for i in text:
        outx = (i['text'])
        outl.append(outx)

        with open("data/op.txt", "a") as opf:
            opf.write(outx + "\n")


def get_vid_id(url):
    if "https://www.youtube.com/watch?v=" in url:
        # Find the index where the video ID starts
        start_index = url.index("https://www.youtube.com/watch?v=") + len("https://www.youtube.com/watch?v=")

        # Extract the video ID
        video_id = url[start_index:start_index + 11]

        if video_id.startswith('-'):
            video_id = '\\' + video_id

        return video_id
    else:
        return None




# url = input("Enter Video Link: ")
#
# id = get_vid_id(url)

# if url:
#     print("Video ID:", id)
# else:
#     print("Video ID not found.")

# create_link_text(id)

query = input("Enter Query: ")
documents = SimpleDirectoryReader('./data').load_data()

index = GPTVectorStoreIndex(documents)

engine = index.as_query_engine()
response = engine.query(query)
print(response)

##Que es Aglae Ekosystem
##NO link required again <----
##https://www.youtube.com/watch?v=vgbMR0lDQBI  STEP2

##https://www.youtube.com/watch?v=TwipifOVZUw   STEP1
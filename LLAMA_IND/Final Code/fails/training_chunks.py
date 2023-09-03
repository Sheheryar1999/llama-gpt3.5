import textract
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import GPT2TokenizerFast

doc = textract.process("../data")
with open('text.txt', 'w') as f:
    f.write(doc.decode('utf-8'))

with open('text.txt', 'r') as f:
    text = f.read()

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text))

# Step 4: Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1024,
    chunk_overlap  = 0,
    length_function = count_tokens,
)

chunks = text_splitter.create_documents([text])
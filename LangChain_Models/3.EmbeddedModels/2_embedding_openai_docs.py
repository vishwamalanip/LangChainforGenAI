from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Es sala cup Namde",
    "RCB we will always support you",
    "ViratKohli is King"
]

result = embedding.embed_documents(documents)

print(str(result))
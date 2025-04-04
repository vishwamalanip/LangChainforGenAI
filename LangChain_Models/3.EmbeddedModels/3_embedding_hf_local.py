from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

#documents = [
#    "Es sala cup Namde",
 #   "RCB we will always support you",
 #  "ViratKohli is King"
#]

#vector = embedding.embed_documents(documents)
text ="Es sala cup Namde"

vector = embedding.embed_query(text)
print(str(vector))
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("customer_support_knowledge_base.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents =[]
    ids = []
    for i, row in df.iterrows():
        doc = Document(
            page_content=row["Category"] + "" + row["Answer"]+""+row["Question"],  # this is the column names of the csv file that you need to read
            metadata={"Category": row["Category"]}
        )
        ids.append(str(i))
        documents.append(doc)

vector_store  = Chroma (
    collection_name="ecommerce_support",
    persist_directory=db_location,
    embedding_function=embeddings,
    )

if add_documents:
    vector_store.add_documents(documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # Adjust k as needed
)



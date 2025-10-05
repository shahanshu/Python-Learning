# import libs
from langchain_community.embeddings import SentenceTransformerEmbeddings

from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate



from langchain.vectorstores import Chroma
from langchain_core.documents import Document

documents = [
    Document(
        page_content="the earth is the only livable planet in the earth and thus "
    ),
    Document(
        page_content="sun and the earth are the most closet to each other and hence they are the most common place to live in the planet and that is why sun is considered the most "
    ),
    Document(
        page_content="Pizza is an Italian dish made of dough, sauce, cheese, and various toppings, baked in an oven."
    )
]
#define embedding models 

embedding_model= SentenceTransformerEmbeddings()


#create chroma vector store in memory 
vectorestore= Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="retivers",
    persist_directory="./retivers_db" 
)

# create a chromaDb hereBy 


vectorestore.add_documents(documents)

#convert the vectore store in retiver
retriever = vectorestore.as_retriever(search_kwargs={"k": 2})


query=" what is closet to the earth"

result= retriever.get_relevant_documents(query)
for i, docs in enumerate(result):
    print(f"\n { i}")
    print(f"{query} \n ")
    print(f"{docs.page_content}")
    i=i+1
    
    
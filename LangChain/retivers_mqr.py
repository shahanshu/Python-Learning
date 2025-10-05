from langchain.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.retrievers import MultiQueryRetriever
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"})
]


# define embedding model
embedding_model= SentenceTransformerEmbeddings()


#define the vectorstore

vectorstore=Chroma.from_documents(
    documents=all_docs,
    embedding=embedding_model
  

)
model = ChatGroq(
    model="openai/gpt-oss-120b",  # use a Groq-supported model
    temperature=0,
)


#create a retiver ( simple )
retiver_old= vectorstore.as_retriever(
  search_type="similarity",
   search_kwargs={"k":5}
    
)



#create a multi query retiver 
mqr= MultiQueryRetriever.from_llm(
    llm= model,
    retriever=vectorstore.as_retriever(  search_kwargs={"k":5})
)

#define the query

query="How to improve energy and mantain the balance ?"


result_trad= retiver_old.get_relevant_documents(query)


result_mrq = mqr.get_relevant_documents(query)


for i, doc in enumerate(result_trad):
    print(f"\n{i+1}------")
    print(f"{doc.page_content}")
for i, doc in enumerate(result_mrq):
    print(f"\n{i+1}------")
    print(f"{doc.page_content}")
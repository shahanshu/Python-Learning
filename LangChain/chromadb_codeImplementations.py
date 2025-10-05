from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv
from langchain_community.embeddings import SentenceTransformerEmbeddings
load_dotenv()



# Create Document objects
doc_math = Document(
    page_content="Mathematics is the study of numbers, shapes, and patterns.",
    metadata={"subject": "Mathematics"}
)

doc_physics = Document(
    page_content="Physics explores matter, energy, and the laws of nature.",
    metadata={"subject": "Physics"}
)

doc_chemistry = Document(
    page_content="Chemistry is the science of substances, their properties, and reactions.",
    metadata={"subject": "Chemistry"}
)

doc_biology = Document(
    page_content="Biology is the study of living organisms and life processes.",
    metadata={"subject": "Biology"}
)

doc_astronomy = Document(
    page_content="Astronomy is the study of celestial objects, space, and the universe.",
    metadata={"subject": "Astronomy"}
)

doc_geology = Document(
    page_content="Geology examines the Earth, its materials, and the processes shaping it.",
    metadata={"subject": "Geology"}
)


docs = [doc_math, doc_physics, doc_chemistry, doc_biology, doc_astronomy, doc_geology]


# choose embedding model 
embedding_functioned = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


#3. create a vectore store 

vectore_store= Chroma(
    embedding_function= embedding_functioned,
    persist_directory='chroma_db',
    collection_name='chroma'
)

#add documents

# persist_directory="./retivers_db" 

'''
results = vectore_store.get(include=["embeddings","documents", "metadatas"])
print(results)
'''
check = vectore_store.similarity_search_with_score(
    "which one is related to the netwons laws",
    k=4
)
for i ,score in check:
    print(f"score : {score:4f} \n content - {i.page_content} the lower the score the better the doc " )
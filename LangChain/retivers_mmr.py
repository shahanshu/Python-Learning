from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document

from langchain.vectorstores import Chroma
# Load environment variables (if needed)
load_dotenv()

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain Supports Chroma, FAISS, Pinecone, and more."),
]

# Initialize embedding model
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")



vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.5}
)
# Run a query
query = "What does LangChain support?"
results = retriever.get_relevant_documents(query)

print("\nQuery:", query)
print("Top Results:")
for i, doc in enumerate(results, 1):
    print(f"{i}. {doc.page_content}")

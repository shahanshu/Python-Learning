from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.retrievers import WikipediaRetriever

# Load environment variables
load_dotenv()

# Initialize the retriever
retriver = WikipediaRetriever(lang="en", top_k_results=3)

# Define the query
query = "who won in the anglo war either nepal or britain"

# Get relevant documents (✅ correct method)
docs = retriver.invoke(query)

# Print retrieved documents
for i, doc in enumerate(docs):
    print(f"\n------ {i+1}th retrieved result ------\n")
    print(doc.page_content)

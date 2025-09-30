from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

text = """My name is anshu shah. i'm 21 years old engineering student at ioe dharan . I like to work with langchain to build the ai models for businesses and the other companies such that it make me wounder the limitatiobs of myself and hence i love working with langchain . Thanks """

splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=2
    
    
)



chunks = splitter.split_text(text)


print(chunks)               



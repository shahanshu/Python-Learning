#1. import the libraries 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
# 2. initialize the llm

model = ChatGroq(
    model="openai/gpt-oss-120b",  
    temperature=0,
)
#3. define the prompt template 
temp1 =PromptTemplate(
  template=" write a detailed report in {topic}",

    input_variables=["topic"]

 
 )

temp2= PromptTemplate(
    template='write a line summary of the followinf text . /n{text}',
    input_variables=["topic"]
)

parser = StrOutputParser()
chain = temp1 | model | parser |temp2 |model | parser

response = chain.invoke({"topic":"blackhole"})
print(response)
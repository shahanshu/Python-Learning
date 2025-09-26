# import libraries 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# define the prompt template 
prompt = PromptTemplate(
    template="Genearte five interesting facts about {topic} ",
    input_variables=['topic']
)
    
#initializa the llm model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=1
)

#define the parser 

parser = StrOutputParser()

chain = prompt | model | parser


# while invoking the chain provide what is being asked in the topic or in the input variables 

result = chain.invoke(
    {
       'topic':'brain'
    }
)


result= chain.invoke(input)
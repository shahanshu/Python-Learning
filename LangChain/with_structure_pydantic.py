from langchain_groq import ChatGroq


from modelspydantic import BaseModel
from typing import Optional,Literal
from dotenv import load_dotenv
load_dotenv()

model= ChatGroq(
   
    model="openai/gpt-oss-120b",  # use a Groq-supported model
    temperature=0,
)

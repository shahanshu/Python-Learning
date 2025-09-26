from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
from typing import Annotated, Literal

model= ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

class anshu(BaseModel):
    name:str= Field(description="Describe the perosn from the text ")
    nature:str = Field(description="descrribe the nature of the person ")


parser= PydanticOutputParser(
    pydantic_object=anshu
)
format_instructions = parser.get_format_instructions()

temp = PromptTemplate(
    template="write a summary on {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions':format_instructions}
 )

chain = temp | model | parser
response = chain.invoke({
    "topic":"ilvia (born Silvia Renate Sommerlath; 23 December 1943) is Queen of Sweden as the wife of King Carl XVI Gustaf. She has held this title since her marriage to Carl XVI Gustaf in 1976. The king and queen have three children: Crown Princess Victoria, Prince Carl Philip, and Princess Madeleine."

})
print(response)
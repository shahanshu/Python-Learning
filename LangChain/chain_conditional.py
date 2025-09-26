from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

from langchain_core.output_parsers import PydanticOutputParser



from pydantic import BaseModel,Field
from typing import Annotated,Literal


load_dotenv()

model= ChatGroq(
    model= "moonshotai/kimi-k2-instruct-0905"
)
parser= StrOutputParser()



'''
prompt = PromptTemplate(
    template=" classify the sentimate from the following {feedback}",
    input_variables=['feedback']
)

'''
class prompt(BaseModel):
    feedback:Literal['positive','negative','neutral'] = Field(description="Provide the sentimente of the feedback")
parser2= PydanticOutputParser(pydantic_object=prompt)




classify= prompt | model | parser
response= classify.invoke({
    'feedback':' this is fucking the best phone that i ever had '
})
print(response)
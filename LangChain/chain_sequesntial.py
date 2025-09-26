from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


model= ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
    )
prompt1 = PromptTemplate(
    template="summarize the {topic} in a paragraph",
    input_variables=['topic']

)

prompt2= PromptTemplate(
    template="summarize the {text} in five points",
    input_variables=['text']

)

parser= StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
response = chain.invoke(
    {
        "topic":'tonk stark '
    }
)
chain.get_graph().print_ascii()
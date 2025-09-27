from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

model =ChatGroq(

    model= "openai/gpt-oss-120b",
    temperature=1.7

        )

prompt = PromptTemplate(
    template=" write a joke about the {topic}",
    input_variables=['topic']

)

prompt2= PromptTemplate(
    
    template=" Explain the {joke}",
    input_variables=['jooke']
)
parser= StrOutputParser()

chain =RunnableSequence(prompt, model,parser,prompt2,model,parser
                        )
response = chain.invoke(
    {
        'topic':'llm'
    }
)
chain.get_graph().print_ascii()
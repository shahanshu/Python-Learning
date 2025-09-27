from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableParallel,RunnableSequence

model= ChatGroq(
    model= "openai/gpt-oss-120b",
    temperature= 0
)

parser= StrOutputParser()

prompt1= PromptTemplate(
    template=" generate a linked post  on {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="generate a five point summary for the job vacancy {topic}",
    input_variables=['topic']
)

'''
 RunnableParallel takes the dict of two sequences overally
'''

parallel_chain= RunnableParallel({
    'topic':RunnableSequence(prompt1,model,parser),
    'report':RunnableSequence(prompt2,model,parser)
})

response= parallel_chain.invoke({
    'topic':'ai'
})
print(response)
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain_core.runnables import RunnableParallel, RunnableSequence,RunnablePassthrough

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
parser= StrOutputParser()

prompt1=PromptTemplate(
    template=" Generate a joke on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template=" Briefly explain the {joke}",
    input_variables=['joke']
)

chain_joke_gen= RunnableSequence(prompt1,model,parser)

chain_parallel= RunnableParallel(
    {
        'joke':RunnableSequence(prompt2,model,parser),
        'summary':RunnablePassthrough(),
    }
)


chain_final= RunnableSequence(chain_joke_gen,chain_parallel)


response= chain_final.invoke({
    'topic':'human brain'

})

print(response['summary'])
print(response['joke'])
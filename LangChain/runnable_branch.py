from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnableBranch, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()


prompt1= PromptTemplate(
    template=" summarize the context {topic}",
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template="Summarize the {summarized} texts in 10 sentences ",
    input_variables=['summarized']
)
parser= StrOutputParser()



model = ChatGroq(
    model="openai/gpt-oss-120b",  # use a Groq-supported model
    temperature=0,
)


chain_repo_gen= prompt1 | model | parser



""" runnableBranch teakes the tupples of as many as the conditions as tupple ( condition, runnables )

"""
chain_branch= RunnableBranch(
    
    (lambda word: len(word.split())>10,RunnableSequence(prompt2,model,parser)),
    
    RunnablePassthrough()
    
)

chain_final= chain_repo_gen | chain_branch
response = chain_final.invoke({
    'topic':'human brain'
})

print((response))
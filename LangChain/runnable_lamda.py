'''
 RunnableLamda is nothing but a runnable that takes function ( lamda sunctions)
'''



from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

prompt1=PromptTemplate(
    template=" Generate a joke on {topic}",
    input_variables=['topic']
)

model = ChatGroq(
    model="openai/gpt-oss-120b",  # use a Groq-supported model
    temperature=0,
)
parser= StrOutputParser()
chain_gen_joke = prompt1 | model | parser


def word_count(texx):
    return(len(texx.split()))

chain_parallel= RunnableParallel({
    'joke':RunnablePassthrough(),
    'word':RunnableLambda(word_count)
})


chain_final=chain_gen_joke | chain_parallel

response= chain_final.invoke({
    'topic':'ai'
})
final_result ="""{} \n word counts -{}""".format(response['joke'],response['word'])

print(final_result)
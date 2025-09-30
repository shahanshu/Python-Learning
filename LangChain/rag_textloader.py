from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


file = TextLoader('demo_file.txt')
bioe=file.load()
bioed= bioe[0].page_content
model = ChatGroq(
    model="openai/gpt-oss-120b",  # use a Groq-supported model
    temperature=0,
)

prompt = PromptTemplate(
    template="what does the person is saying about himself in the content {bio}",
    input_variables=['bio']
)

parser=StrOutputParser()

chain= prompt |model |parser

response= chain.invoke({
    'bio':bioed
})


formatted = " the person is {}".format(response)
print(formatted)














# 1. Import libraries
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

# 2. Initialize the LLM
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# 3. Setup JSON parser
parser = JsonOutputParser()

# 4. Define prompt template
temp = PromptTemplate(
    template="Give me the name of {topic}.\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)


chain = temp | model | parser
response = chain.invoke({"topic":"10  fictional heros "})
print(response)
print(type(response))
first = response['heroes'][3]
print(first)
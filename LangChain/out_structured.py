from langchain_groq import ChatGroq
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables (make sure GROQ_API_KEY is set in your .env file)
load_dotenv()

# Initialize model
model = ChatGroq(
    model="openai/gpt-oss-120b",  # or another Groq-supported model
    temperature=0
)

# Define schema
schema = [
    ResponseSchema(name="fact-1 \n" , description="first fact of topic"),
    ResponseSchema(name="fact-2 \n", description="second fact of topic"),
    ResponseSchema(name="fact-3 \n", description="third fact of topic")
]

# Create parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Create prompt
template = PromptTemplate(
    template="Give 3 facts about the {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Build chain
chain = template | model | parser

# Run chain
response = chain.invoke({"topic": "human body"})
print(response)

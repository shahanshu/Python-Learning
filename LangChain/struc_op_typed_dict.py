from typing import TypedDict, Literal ,Annotated
import langchain
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Step 1: Define schema with TypedDict
class ReviewAnalysis(TypedDict):
    summary: Annotated[Literal["worht it ","not worth it"],'Abrief summary of the review ']
    sentiment: Annotated[int,"return 1 for positive,0 for neutral and -1 for negative "]
  
# Step 2: Setup Groq LLM
model = ChatGroq(
    model="openai/gpt-oss-120b",  # use a Groq-supported model
    temperature=0,
)

# Step 3: Wrap with structured output
structured_llm = model.with_structured_output(ReviewAnalysis)

# Step 4: Call the structured LLM
review = "The battery is worth the money but the delivery wasn't good and also the condition of the packaging  wan't very good "
result = structured_llm.invoke(review)

# Step 5: Access fields

print(result)

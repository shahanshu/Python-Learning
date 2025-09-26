from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

# Define models
model1 = ChatGroq(model="moonshotai/kimi-k2-instruct-0905", temperature=0)
model2 = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

# Prompt to generate notes
prompt = PromptTemplate(
    template="Generate detailed notes on the topic: {topic}",
    input_variables=['topic']
)

# Prompt to generate quiz
prompt2 = PromptTemplate(
    template="Generate five short questions based on the topic: {topic}",
    input_variables=['topic']
)

# Prompt to merge notes and quiz
prompt3 = PromptTemplate(
    template="Merge the provided notes and the quiz into a single document.\n\nNotes:\n{notes}\n\nQuiz:\n{quiz}",
    input_variables=['notes', 'quiz']
)

# Parser
parser = StrOutputParser()

# Run notes and quiz generation in parallel
parallel_chain = RunnableParallel({
    'notes': prompt | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# Merge chain
merge_chain = prompt3 | model2 | parser

# Combine everything
chain = parallel_chain | merge_chain

# Input topic
topic = """
SVM is short for Support Vector Machine, a supervised machine learning algorithm used for both classification and regression tasks by finding the optimal hyperplane (a decision boundary) that best separates different classes of data...
"""

# Run the final chain
result = chain.invoke({'topic': topic})

print(result)

chain.get_graph().print_ascii()
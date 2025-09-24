import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import sys

# 1. Load environment variables
load_dotenv()

# 2. Initialize Groq LLM with error handling
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("Error: GROQ_API_KEY not found in environment variables.")
    sys.exit(1)

try:
    llm = ChatGroq(
        api_key=groq_api_key,
        model="openai/gpt-oss-20b",  # Updated to a current model
        temperature=0.7
    )
except Exception as e:
    print(f"Error initializing Groq client: {e}")
    sys.exit(1)

# 3. Create a Chat Prompt Template with conversation history
def create_conversation_chain():
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Keep responses concise but informative."),
        ("human", "{user_input}")
    ])

def chat_with_ai():
    print("🤖 AI Assistant: Hello! I'm your helpful AI assistant. Type 'quit' or 'exit' to end the conversation.")
    print("-" * 60)
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit conditions
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🤖 AI Assistant: Goodbye! 👋")
                break
            
            if not user_input:
                print("Please enter a message.")
                continue
            
            # Create prompt with current input
            prompt_template = create_conversation_chain()
            formatted_prompt = prompt_template.format_messages(user_input=user_input)
            
            # Get AI response
            print("🤖 AI Assistant: ", end="", flush=True)
            response = llm.invoke(formatted_prompt)
            
            # Print the response
            print(response.content)
            
        except KeyboardInterrupt:
            print("\n\n🤖 AI Assistant: Conversation interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.")

# Alternative version with streaming response (more interactive)
def chat_with_ai_streaming():
    print("🤖 AI Assistant: Hello! I'm your helpful AI assistant (Streaming Mode).")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🤖 AI Assistant: Goodbye! 👋")
                break
            
            if not user_input:
                print("Please enter a message.")
                continue
            
            prompt_template = create_conversation_chain()
            formatted_prompt = prompt_template.format_messages(user_input=user_input)
            
            print("🤖 AI Assistant: ", end="", flush=True)
            
            # Use streaming for more interactive feel
            for chunk in llm.stream(formatted_prompt):
                print(chunk.content, end="", flush=True)
            print()  # New line after response
            
        except KeyboardInterrupt:
            print("\n\n🤖 AI Assistant: Conversation interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    print("Choose conversation mode:")
    print("1. Standard mode")
    print("2. Streaming mode (more interactive)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "2":
        chat_with_ai_streaming()
    else:
        chat_with_ai()
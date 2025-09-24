import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import json
from datetime import datetime

# Load environment variables
load_dotenv()

class ChatHistoryManager:
    """Manages chat history storage and retrieval"""
    
    def __init__(self, history_file="chat_history.txt"):
        self.history_file = history_file
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create history file if it doesn't exist"""
        if not os.path.exists(self.history_file):
            with open(self.history_file, 'w') as f:
                json.dump([], f)
    
    def save_message(self, role, content):
        """Save a message to history file"""
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
        except:
            history = []
        
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        
        history.append(message)
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def load_history(self):
        """Load chat history from file"""
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
            return history
        except:
            return []
    
    def get_formatted_history(self):
        """Get history formatted for LangChain memory"""
        history = self.load_history()
        messages = []
        
        for msg in history:
            if msg["role"] == "human":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "ai":
                messages.append(AIMessage(content=msg["content"]))
        
        return messages

class GroqChatChain:
    def __init__(self, model_name="openai/gpt-oss-20b"):
        # Initialize Groq chat model
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=model_name
        )
        
        # Initialize chat history manager
        self.history_manager = ChatHistoryManager()
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant. Have a natural conversation while being helpful and concise.
             
             Current conversation history:
             {history}
             
             Human: {input}
             AI:"""),
        ])
        
        # Initialize memory with loaded history
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="history"
        )
        
        # Load existing history into memory
        self._load_history_to_memory()
        
        # Create conversation chain
        self.conversation = ConversationChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory,
            verbose=False
        )
    
    def _load_history_to_memory(self):
        """Load existing chat history into memory"""
        formatted_history = self.history_manager.get_formatted_history()
        for message in formatted_history:
            if isinstance(message, HumanMessage):
                self.memory.chat_memory.add_user_message(message.content)
            elif isinstance(message, AIMessage):
                self.memory.chat_memory.add_ai_message(message.content)
    
    def chat(self, message):
        """Send a message and get response"""
        # Get response from the model
        response = self.conversation.predict(input=message)
        
        # Save both messages to history
        self.history_manager.save_message("human", message)
        self.history_manager.save_message("ai", response)
        
        return response
    
    def get_chat_history(self):
        """Get formatted chat history"""
        return self.history_manager.load_history()
    
    def clear_history(self):
        """Clear chat history"""
        with open(self.history_manager.history_file, 'w') as f:
            json.dump([], f)
        self.memory.clear()

# Alternative implementation using Message template approach
class GroqMessageTemplateChain:
    def __init__(self, model_name="openai/gpt-oss-20b"):
        load_dotenv()
        
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=model_name
        )
        
        self.history_manager = ChatHistoryManager()
        
        # Message template for more structured responses
        self.message_template = ChatPromptTemplate.from_messages([
            ("system", """You are an AI assistant. Analyze the conversation history and provide a helpful response.
             
             Conversation History:
             {history}
             
             Current Message: {input}
             
             Please provide a clear and helpful response."""),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
    
    def get_response(self, message):
        """Get response using message template"""
        # Load history
        history_messages = self.history_manager.get_formatted_history()
        
        # Format prompt
        formatted_prompt = self.message_template.format_messages(
            history=history_messages,
            input=message
        )
        
        # Get response
        response = self.llm.invoke(formatted_prompt)
        
        # Save to history
        self.history_manager.save_message("human", message)
        self.history_manager.save_message("ai", response.content)
        
        return response.content

# Usage example
def main():
    # Initialize the chat chain
    chat_chain = GroqChatChain(model_name="openai/gpt-oss-20b")
    
    # Or use the message template version
    # chat_chain = GroqMessageTemplateChain(model_name="mixtral-8x7b-32768")
    

    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            break
        
        response = chat_chain.chat(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    # Create .env file with your Groq API key if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write('GROQ_API_KEY=your_groq_api_key_here\n')
        print("Please add your Groq API key to the .env file")
    else:
        main()
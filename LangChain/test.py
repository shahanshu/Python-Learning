import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from dotenv import load_dotenv
import os
import json
import time

# Load environment variables
load_dotenv()

# Load prompt templates from JSON file
def load_prompt_templates():
    try:
        with open('prompt.json', 'r') as f:
            prompts_data = json.load(f)
        return prompts_data
    except FileNotFoundError:
        st.error("prompt.json file not found. Please make sure it exists in the same directory.")
        return None
    except json.JSONDecodeError:
        st.error("Error parsing prompt.json. Please check the file format.")
        return None

# Initialize prompt templates from JSON data
def initialize_templates(prompts_data):
    templates = {}
    
    for template_name, template_config in prompts_data["templates"].items():
        messages = []
        if "system" in template_config:
            messages.append(("system", template_config["system"]))
        messages.append(("human", template_config["human"]))
        templates[template_name] = ChatPromptTemplate.from_messages(messages)
    
    return templates

# Set page config
st.set_page_config(
    page_title="Moksha Ai - Dynamic Prompting",
    page_icon="🤖",
    layout="centered"
)

# Initialize model
@st.cache_resource
def load_model():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

# Custom CSS for smooth scrolling and better styling
def inject_custom_css():
    st.markdown("""
    <style>
    /* Smooth scrolling for the entire app */
    html {
        scroll-behavior: smooth;
    }
    
    /* Custom scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    
    /* Chat message styling */
    .stChatMessage {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 8px;
        animation: fadeIn 0.3s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Smooth transitions for chat messages */
    .chat-fade-in {
        animation: fadeIn 0.5s ease-in-out;
    }
    
    /* Custom container for chat messages with smooth scrolling */
    .chat-container {
        max-height: 70vh;
        overflow-y: auto;
        padding: 10px;
        border-radius: 10px;
        background-color: #fafafa;
        margin-bottom: 20px;
        scroll-behavior: smooth;
    }
    
    /* Ensure proper spacing */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# JavaScript for auto-scrolling to bottom
def auto_scroll_to_bottom():
    st.markdown("""
    <script>
    // Function to scroll to bottom of chat
    function scrollToBottom() {
        const chatContainer = document.querySelector('.chat-container') || document.querySelector('.main');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }
    
    // Scroll when page loads
    window.addEventListener('load', function() {
        setTimeout(scrollToBottom, 100);
    });
    
    // Scroll when new messages are added
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                setTimeout(scrollToBottom, 300);
            }
        });
    });
    
    // Start observing when DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        const targetNode = document.querySelector('.main') || document.body;
        if (targetNode) {
            observer.observe(targetNode, { childList: true, subtree: true });
        }
    });
    </script>
    """, unsafe_allow_html=True)

def main():
    # Inject custom CSS
    inject_custom_css()
    
    # Load prompt data
    prompts_data = load_prompt_templates()
    if prompts_data is None:
        st.stop()
    
    # Initialize templates
    PROMPT_TEMPLATES = initialize_templates(prompts_data)
    EXAMPLES = prompts_data.get("examples", [])
    DEFAULT_SETTINGS = prompts_data.get("default_settings", {})
    
    # Initialize few-shot prompt template
    example_prompt = ChatPromptTemplate.from_messages([
        ("human", "{input}"), 
        ("ai", "{output}")
    ])
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt, 
        examples=EXAMPLES
    )

    def build_prompt(user_input, template_choice, few_shot, use_context, custom_instructions, history):
        messages = []

        # Custom instructions
        if custom_instructions:
            messages.append(("system", f"Additional instructions: {custom_instructions}"))

        # Few-shot examples
        if few_shot:
            few_shot_messages = few_shot_prompt.format_messages()
            for msg in few_shot_messages:
                messages.append((msg.type, msg.content))

        # Context from conversation history
        if use_context and history:
            for msg in history[-3:]:  # Last 3 messages for context
                role = "human" if msg["role"] == "user" else "ai"
                messages.append((role, msg["content"]))

        # Base template
        base_messages = PROMPT_TEMPLATES[template_choice].format_messages(input=user_input)
        for msg in base_messages:
            messages.append((msg.type, msg.content))

        return ChatPromptTemplate.from_messages(messages)

    st.title("🤖 Moksha Ai - Dynamic Prompting")

    # Session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "last_message_count" not in st.session_state:
        st.session_state.last_message_count = 0

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")

        template_choice = st.selectbox(
            "Prompt Template", 
            list(PROMPT_TEMPLATES.keys()), 
            index=list(PROMPT_TEMPLATES.keys()).index(DEFAULT_SETTINGS.get("template_choice", "default"))
        )
        few_shot = st.checkbox("Use Few-Shot Examples", value=DEFAULT_SETTINGS.get("few_shot", False))
        use_context = st.checkbox("Use Conversation Context", value=DEFAULT_SETTINGS.get("use_context", True))
        custom_instructions = st.text_area(
            "Custom Instructions", 
            value=DEFAULT_SETTINGS.get("custom_instructions", ""),
            placeholder="Add extra instructions..."
        )

        st.header("📊 Template Info")
        st.write(f"Available templates: {', '.join(PROMPT_TEMPLATES.keys())}")
        st.write(f"Few-shot examples: {len(EXAMPLES)}")
        
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.session_state.last_message_count = 0
            st.rerun()

    # Chat container with smooth scrolling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Chat messages with smooth appearance
    for i, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"]):
            # Add fade-in effect for new messages
            if i >= st.session_state.last_message_count:
                st.markdown(f'<div class="chat-fade-in">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Input
    if prompt := st.chat_input("Type your message..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-fade-in">{prompt}</div>', unsafe_allow_html=True)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    model = load_model()
                    dynamic_prompt = build_prompt(
                        user_input=prompt,
                        template_choice=template_choice,
                        few_shot=few_shot,
                        use_context=use_context,
                        custom_instructions=custom_instructions,
                        history=st.session_state.messages
                    )
                    formatted_messages = dynamic_prompt.format_messages(input=prompt)
                    response = model.invoke(formatted_messages)
                    
                    # Stream the response for smoother appearance
                    response_text = response.content
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    for chunk in response_text.split():
                        full_response += chunk + " "
                        message_placeholder.markdown(f'<div class="chat-fade-in">{full_response}▌</div>', unsafe_allow_html=True)
                        time.sleep(0.05)  # Adjust speed here
                    
                    message_placeholder.markdown(f'<div class="chat-fade-in">{full_response}</div>', unsafe_allow_html=True)
                    
                    st.session_state.messages.append({"role": "assistant", "content": full_response.strip()})
                    
                except Exception as e:
                    st.error(f"Error: {e}")

        # Update message count and trigger scroll
        st.session_state.last_message_count = len(st.session_state.messages)
        
        # Auto-scroll to bottom after new message
        auto_scroll_to_bottom()
        
        # Small delay to ensure DOM is updated before scrolling
        time.sleep(0.1)

    # Display current configuration
    with st.expander("Current Prompt Configuration"):
        st.json({
            "selected_template": template_choice,
            "few_shot_enabled": few_shot,
            "context_enabled": use_context,
            "custom_instructions": custom_instructions,
            "chat_history_length": len(st.session_state.messages)
        })

    # Initial scroll to bottom on page load
    if st.session_state.messages:
        auto_scroll_to_bottom()

if __name__ == "__main__":
    main()
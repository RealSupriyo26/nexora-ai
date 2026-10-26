import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="Nexora AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# App Header
st.title("🤖 Nexora AI Assistant")
st.write("আপনার নিজের প্রিমিয়াম এআই চ্যাট অ্যাপ্লিকেশন!")

# Initialize Groq Client
API_KEY = "guUfL0nY5akP7vd1rmyMu"

if not API_KEY:
    st.warning("⚠️ দয়া করে আপনার Groq API Key দিন।")
else:
    client = Groq(api_key=API_KEY)

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display prior chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("আপনার কি জানার আছে বলুন..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response from Groq AI
        with st.chat_message("assistant"):
            try:
                chat_completion = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                )
                response = chat_completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"ত্রুটি দেখা দিয়েছে: {e}")
							

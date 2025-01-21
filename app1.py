import streamlit as st

# Title of the application
st.title("Simple Chatbot")

# Introduction message
st.write("Hi there! I'm a simple chatbot. Ask me anything, and I'll try to help!")

# Input from user
user_input = st.text_input("Your question:")

# Simple chatbot logic
if user_input:
    if "hello" in user_input.lower():
        st.write("Hello! How can I assist you today?")
    elif "your name" in user_input.lower():
        st.write("I'm your friendly chatbot! I don't have a fancy name yet.")
    elif "weather" in user_input.lower():
        st.write("I'm not sure about the weather right now. You can try checking a weather app!")
    elif "bye" in user_input.lower():
        st.write("Goodbye! Have a great day!")
    else:
        st.write("Hmm, I don't understand that yet. Try asking something else!")

# Footer message
st.write("I'm still learning, so my responses are limited. Thanks for chatting!")

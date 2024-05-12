import streamlit as st

# Function to generate a quiz form
def generate_quiz(topic, num_questions, num_options):
    st.header(f"{topic} Quiz")
    user_answers = {}
    
    for q in range(1, num_questions + 1):
        st.subheader(f"Question {q}")
        question = st.text_input(f"Enter question {q}", key=f"Q{q}")
        
        options = [st.text_input(f"Option {i+1} for question {q}", key=f"Q{q}O{i}") for i in range(num_options)]
        answer = st.radio(f"Choose the correct answer for question {q}", options, key=f"Ans{q}")
        
        user_answers[question] = answer
    
    if st.button('Submit Quiz'):
        st.write("You've completed the quiz! Here are your answers:")
        for question, answer in user_answers.items():
            st.write(f"{question}: {answer}")

# Streamlit app layout
st.title("Dynamic Quiz Generator")

# User inputs for quiz configuration
topic = st.text_input("Enter the topic for the quiz:")
num_questions = st.number_input("How many questions do you need?", min_value=1, max_value=15, step=1)
num_options = st.number_input("How many possible answers to each question do you need?", min_value=1, max_value=5, step=1)

if st.button("Start Quiz"):
    generate_quiz(topic, int(num_questions), int(num_options))

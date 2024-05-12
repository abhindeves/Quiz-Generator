
import streamlit as st 
from teacher import Teacher
from test_creator import TestGenerator
from exam_simulator import Exam

# Initialize session state for storing answers, questions, and options
if 'student_answer' not in st.session_state:
    st.session_state['student_answer'] = {}
if 'answer_key' not in st.session_state:
    st.session_state['answer_key'] = {}
if 'questions_and_options' not in st.session_state:
    st.session_state['questions_and_options'] = {}

# Streamlit app layout
st.title("🎓 Dynamic Quiz Generator 🎓")

# User inputs for quiz configuration
topic = st.text_input("📚 Enter the topic for the quiz:")
num_questions = st.number_input("🔢 How many questions do you need?", min_value=1, max_value=15, step=1)
num_options = st.number_input("🔄 How many possible answers to each question do you need?", min_value=2, max_value=5, step=1)

# Function to handle the final submission of answers
def handle_final_submission():
    st.balloons()
    st.success("🎉 Congratulations! You've completed the quiz! 🎉")

def grade():
    answer_key = st.session_state.answer_key
    student_answers = st.session_state.student_answer
    score = 0
    for question, answer in answer_key.items():
        correct_answer = answer.split('Answer:')[1].strip()[0]
        if student_answers[question].split(')')[0] == correct_answer.lower():
            score += 1
    return score

# Generate and store the quiz questions and options in session state
def generate_quiz():
    with st.spinner('Generating your personalized quiz...'):
        test_gen = TestGenerator(topic, num_questions, num_options)
        teacher = Teacher()
        test = test_gen.run()
        student_view = teacher.create_student_view(test, num_questions)
        answer_key = teacher.extract_answers(test, num_questions)
        st.session_state['questions_and_options'] = student_view
        st.session_state['answer_key'] = answer_key

# Start the quiz
if st.button("🚀 Start Quiz"):
    generate_quiz()

# Display the quiz if it has been generated
if st.session_state['questions_and_options']:
    st.header(f"📝 {topic} Quiz")
    progress_bar = st.progress(0)
    for i, (question, options) in enumerate(st.session_state['questions_and_options'].items(), start=1):
        # Split the question and options
        question_text = options.split("?")[0]
        options_list = options.split("?")[1].strip().split("\n")
        
        # Display the question
        st.subheader(f"Question {i}")
        st.markdown(f"{question_text}")
        
        # Display options and store the selected answer in session state
        st.session_state.student_answer[question] = st.radio("Choose one:", options_list, key=f"q{i}",index=None)
        progress_bar.progress(i/num_questions)
    st.write("Quiz progress:", i, "/", num_questions)

# Final submission button
if st.button("✅ Submit Answers"):
    handle_final_submission()
    score = grade()
    st.metric(label="Your Score", value=f"{score}/{num_questions}")

# Display the stored answers for review
# if st.session_state.student_answer:
#     st.write("📝 Your answers so far:")
#     for question, answer in st.session_state.student_answer.items():
#         st.write(f"**{question}**: {answer}")


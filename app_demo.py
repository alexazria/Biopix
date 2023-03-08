import streamlit as st
import openai
from apikey import APIKEY

openai.api_key = APIKEY

st.title('Hello, I will help you succeed in your Job Interview! :smiley:')

# Define a function to generate interview questions and answers using the ChatGPT API
def generate_questions_answers(company_name, interview_stage, theoretical_questions, coding_questions, job_description, cv):
    # Define the prompt for the ChatGPT API
    prompt = f"Company Name: {company_name}\n\nInterview Stage: {', '.join(interview_stage)}\n\nTheoretical Questions: {', '.join(theoretical_questions)}\n\nCoding Questions: {', '.join(coding_questions)}\n\nJob Description: {job_description}\n\nCV: {cv}\n\nQ:"
    # Call the ChatGPT API to generate interview questions and answers
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1000024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Extract the generated interview questions and answers from the API response
    output = response.choices[0].text.strip().split("A:")
    questions = [q.strip() for q in output if q.startswith("Q:")]
    answers = [a.strip() for a in output if a.startswith("A:")]
    # Return the generated interview questions and answers
    return questions, answers

with st.form('Job'):
    company_name = st.text_input('Company Name', '')
    interview_stage = st.multiselect('Interview Stage',['Screening Call', 'Assessment Test', 'Second Interview', 'Final Round'],)
    theoretical_questions = st.multiselect('Select how many theoretical questions would you like ?',['0','5', '10', '15', '20'],)
    coding_questions = st.multiselect('If you have a coding interview, select how many coding questions would you like to prepare ?',['0','5', '10', '15', '20'],)
    job_description = st.text_input('Paste the Job Description', '')
    cv = st.text_input('Paste your cv content', '')
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Please wait while we generate your interview questions and answers...")
        # Call the generate_questions_answers function to generate interview questions and answers
        questions, answers = generate_questions_answers(company_name, interview_stage, theoretical_questions, coding_questions, job_description, cv)
        # Display the generated interview questions and answers
        st.write("Here are your interview questions and answers:")
        for i, (q, a) in enumerate(zip(questions, answers)):
            st.write(f"{i+1}. Q: {q}\n   A: {a}")

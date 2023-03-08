api_key="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"
import streamlit as st
import openai
from apikey import APIKEY

st.title('Hello, I will help you suceed your Job Interview !:smiley:')

with st.form('Job'):
    company_name = st.text_input('Company Name', '')
    interview_stage = st.multiselect('Interview Stage',['Screening Call', 'Assessment Test', 'Second Interview', 'Final Round'],)
    theoritical_question = st.multiselect('Select how many questions would you like ?',['0','5', '10', '15', '20'],)
    coding_question = st.multiselect('If you have a coding interview, select how many coding question would you like to prepare ?',['0','5', '10', '15', '20'],)
    job_description = st.text_input('Paste the Job Description', '')
    cv = st.text_input('Paste your cv content', '')
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Wait we are creating your questions and answers")



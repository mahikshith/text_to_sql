import os
import streamlit as st
import sqlite3

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file")


def llm_response(query,prompt):
    model = genai.GenerativeModel("gemini-3-flash-preview")
    response = model.generate_content([prompt,query])
    return response.text

# func to read the generated sql query and connect to db 
def connect_to_db(sql_query,db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql_query)

    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for each_row in all_rows:
        print(each_row)

    return all_rows


# definin the prompt  

prompt = """
You are a database expert and your task is to generate a sql query for the given question.

the sql student database is as follows : 

it contains data about student name , roll number , section and marks.

here are the Example  queries : \n\n example 1 :  if you want to get the total records it should

return like this Select count(*) from STUDENT

\n\n example 2 : if you want to get total marks for students who scored above 85 :

return like this Select sum(marks) from STUDENT where marks > 85 

and make sure that the query generated should not have ``` in beginning or end and sql word in output. 


"""

# streamlit app 

st.set_page_config(page_title="SQL Query Generator and DB connection", page_icon=":tada:")

st.header("Natural language to sql to db connect")

question = st.text_input("Enter your query")

button = st.button("generate answer")

if button:
    sql_query = llm_response(question,prompt)

    print(sql_query)


    st.write(sql_query)


    fp = connect_to_db(sql_query,"studentdatabase.db")

    st.subheader("response from db : ")

    for each_row in fp:

        st.subheader(each_row)

    

    

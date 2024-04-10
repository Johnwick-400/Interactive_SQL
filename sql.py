import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import google.generativeai as genai

def execute_sql_query(df, sql_query):
    temp_db = create_engine('sqlite:///:memory:', echo=False)
    df.to_sql(name='Sales', con=temp_db, index=False)
    with temp_db.connect() as conn:
        result = conn.execute(text(sql_query))
        rows = result.fetchall()
    return rows


def create_prompt(df, nlp_text):
    prompt = f'''Given the following sqlite SQL definition, write queries based on the request:
    ### sqlite SQL table, with its properties:
    # Sales({",".join(str(x) for x in df.columns)})
    A query to answer: {nlp_text}
    '''
    return prompt


def main():
    st.title("Interactive SQL")
    st.markdown("<h3 style='font-size:25px'>Upload, Prompt, Analyze</h3>", unsafe_allow_html=True)

  
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    nlp_text = st.text_input("Enter information you want to obtain:", "")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

     
        prompt = create_prompt(df, nlp_text)

        response = model.generate_content([prompt])
        sql_query = response.text.strip().strip('`sql \n').replace("\n", ' ')

        # Execute SQL query and display result
        if st.button("Execute SQL Query"):
            st.write(sql_query)
            rows = execute_sql_query(df, sql_query)
            st.table(pd.DataFrame(rows))

if __name__ == "__main__":
    # Configure GenAI API
    genai.configure(api_key='YOUR API')  # Replace with your actual API key

    # Initialize GenerativeModel
    model = genai.GenerativeModel('gemini-pro')

    main()

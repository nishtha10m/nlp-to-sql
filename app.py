import streamlit as st
import pandas as pd

from parser import parse_query
from sql_generator import generate_sql
from executor import load_to_sqlite, run_sql

st.title("NLP-to-SQL Converter")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file:
    df = pd.read_csv(file, encoding='latin1')
    st.write("Preview:", df.head())

    columns = list(df.columns)
    st.write("Detected Columns:", columns)

    query = st.text_input("Enter your query (e.g., total sales by city)")

    if st.button("Convert & Run"):
        parsed = parse_query(query, columns)
        sql = generate_sql(parsed, "uploaded", columns)

        if sql:
            st.write("Generated SQL:", sql)
            conn = load_to_sqlite(df)
            try:
                result = run_sql(conn, sql)
                st.write("Result:")
                st.dataframe(result)
            except Exception as e:
                st.error(f"SQL Execution Error: {e}")
        else:
            st.error("Could not generate SQL for this query.")

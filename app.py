import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent,create_spark_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 Langchain Chat with SQL DB")

LOCALDB="USE_LOCALDB"
MYSQL = "USE_MYSQL"

radio_output = ["Use SQLLite 3 Database - Student database","Connect to SQL Database"]

selected_opt = st.sidebar.radio(label="Choose the DB you wanna interact with ",options=radio_output)

if radio_output.index(selected_opt)==1:
    db_uri= MYSQL
    mysql_host = st.sidebar.text_input("Provide MYSQL host")
    mysql_user = st.sidebar.text_input("MYSQL user")
    mysql_password = st.sidebar.text_input("MYSQL password",type="password")
    mysql_db = st.sidebar.text_input("SQL Database")

else:
    db_uri=LOCALDB
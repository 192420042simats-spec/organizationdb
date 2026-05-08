import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(
    page_title="Organ Donation System",
    page_icon="🏥",
    layout="wide"
)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="JAYASHREE@12345678",
    database="organdonationdb"
)

st.title("🏥 Organ Donation and Transplant Matching System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Donor Records",
        "Recipient Records",
        "Hospital Records",
        "Transplant Records"
    ]
)

if menu == "Donor Records":

    st.header("Donor Records")

    query = "SELECT * FROM Donors"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

elif menu == "Recipient Records":

    st.header("Recipient Records")

    query = "SELECT * FROM Recipients"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

elif menu == "Hospital Records":

    st.header("Hospital Records")

    query = "SELECT * FROM Hospitals"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

elif menu == "Transplant Records":

    st.header("Transplant Records")

    query = "SELECT * FROM Transplants"

    df = pd.read_sql(query, conn)

    st.dataframe(df)

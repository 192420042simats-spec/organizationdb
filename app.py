# Full Streamlit App Code for Organ Donation and Transplant Matching System

Copy the FULL code below into `app.py`

```python
import streamlit as st
import mysql.connector
import pandas as pd

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Organ Donation System",
    page_icon="🏥",
    layout="wide"
)

# MYSQL CONNECTION
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="JAYASHREE@12345678",
    database="organdonationdb"
)

cursor = conn.cursor()

# TITLE
st.title("🏥 Organ Donation and Transplant Matching System")

st.markdown("---")

# SIDEBAR
menu = st.sidebar.radio(
    "Navigation Menu",
    [
        "Dashboard",
        "Donor Records",
        "Recipient Records",
        "Hospital Records",
        "Transplant Records",
        "Add Donor",
        "Add Recipient",
        "Search Match"
    ]
)

# DASHBOARD
if menu == "Dashboard":

    st.header("📊 Dashboard")

    # TOTAL DONORS
    cursor.execute("SELECT COUNT(*) FROM Donors")
    donors = cursor.fetchone()[0]

    # TOTAL RECIPIENTS
    cursor.execute("SELECT COUNT(*) FROM Recipients")
    recipients = cursor.fetchone()[0]

    # TOTAL HOSPITALS
    cursor.execute("SELECT COUNT(*) FROM Hospitals")
    hospitals = cursor.fetchone()[0]

    # TOTAL TRANSPLANTS
    cursor.execute("SELECT COUNT(*) FROM Transplants")
    transplants = cursor.fetchone()[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Donors", donors)
    col2.metric("Total Recipients", recipients)
    col3.metric("Hospitals", hospitals)
    col4.metric("Transplants", transplants)

    st.markdown("---")

    st.subheader("System Features")

    st.write("""
    ✅ Donor Management  
    ✅ Recipient Management  
    ✅ Hospital Information  
    ✅ Organ Matching  
    ✅ Transplant Tracking  
    ✅ SQL Database Connection  
    """)

# DONOR RECORDS
elif menu == "Donor Records":

    st.header("🧑 Donor Records")

    query = "SELECT * FROM Donors"

    df = pd.read_sql(query, conn)

    st.dataframe(df, use_container_width=True)

# RECIPIENT RECORDS
elif menu == "Recipient Records":

    st.header("🧑‍⚕ Recipient Records")

    query = "SELECT * FROM Recipients"

    df = pd.read_sql(query, conn)

    st.dataframe(df, use_container_width=True)

# HOSPITAL RECORDS
elif menu == "Hospital Records":

    st.header("🏥 Hospital Records")

    query = "SELECT * FROM Hospitals"

    df = pd.read_sql(query, conn)

    st.dataframe(df, use_container_width=True)

# TRANSPLANT RECORDS
elif menu == "Transplant Records":

    st.header("❤️ Transplant Records")

    query = "SELECT * FROM Transplants"

    df = pd.read_sql(query, conn)

    st.dataframe(df, use_container_width=True)

# ADD DONOR
elif menu == "Add Donor":

    st.header("➕ Add Donor")

    donorcode = st.text_input("Donor Code")
    age = st.number_input("Age", min_value=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    blood = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    organ = st.selectbox(
        "Organ Type",
        ["Kidney", "Liver", "Heart", "Lung", "Cornea", "Pancreas"]
    )

    city = st.text_input("City")
    year = st.number_input("Donation Year", min_value=2020)

    if st.button("Add Donor"):

        sql = """
        INSERT INTO Donors
        (DonorCode, Age, Gender, BloodGroup, OrganType, City, DonationYear)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            donorcode,
            age,
            gender,
            blood,
            organ,
            city,
            year
        )

        cursor.execute(sql, values)
        conn.commit()

        st.success("Donor Added Successfully")

# ADD RECIPIENT
elif menu == "Add Recipient":

    st.header("➕ Add Recipient")

    recipientcode = st.text_input("Recipient Code")
    age = st.number_input("Age", min_value=1)
    gender = st.selectbox("Gender", ["Male", "Female"])

    blood = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    organ = st.selectbox(
        "Required Organ",
        ["Kidney", "Liver", "Heart", "Lung", "Cornea", "Pancreas"]
    )

    urgency = st.selectbox(
        "Urgency Level",
        ["Low", "Medium", "High", "Critical"]
    )

    city = st.text_input("City")

    if st.button("Add Recipient"):

        sql = """
        INSERT INTO Recipients
        (RecipientCode, Age, Gender, BloodGroup, RequiredOrgan, UrgencyLevel, City)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            recipientcode,
            age,
            gender,
            blood,
            organ,
            urgency,
            city
        )

        cursor.execute(sql, values)
        conn.commit()

        st.success("Recipient Added Successfully")

# SEARCH MATCH
elif menu == "Search Match":

    st.header("🔍 Organ Match Search")

    blood = st.selectbox(
        "Select Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    organ = st.selectbox(
        "Select Organ",
        ["Kidney", "Liver", "Heart", "Lung", "Cornea", "Pancreas"]
    )

    if st.button("Search Match"):

        query = f"""
        SELECT
            Donors.DonorCode,
            Donors.BloodGroup,
            Donors.OrganType,
            Donors.City,
            Recipients.RecipientCode,
            Recipients.RequiredOrgan,
            Recipients.UrgencyLevel
        FROM Donors
        JOIN Recipients
        ON Donors.BloodGroup = Recipients.BloodGroup
        WHERE Donors.BloodGroup = '{blood}'
        AND Donors.OrganType = '{organ}'
        """

        df = pd.read_sql(query, conn)

        if len(df) > 0:

            st.success("Matching Records Found")

            st.dataframe(df, use_container_width=True)

        else:

            st.error("No Matching Records Found")
```

# IMPORTANT

Whenever you:

* Add data in MySQL
* Insert new donor
* Insert recipient
* Update hospital table
* Change transplant records

The app automatically shows updated data.

This is because the Streamlit app is directly connected to your MySQL database.

# RUN THE APP

Open terminal:

```bash
streamlit run app.py
```

# OUTPUT YOU WILL GET

* Dashboard
* Donor table
* Recipient table
* Hospital table
* Transplant table
* Add donor form
* Add recipient form
* Search match system
* Dynamic database updates

# FOR PUBLIC USE

After app works:

1. Create GitHub repository
2. Upload app.py
3. Create requirements.txt
4. Deploy in Streamlit Cloud
5. Share public link

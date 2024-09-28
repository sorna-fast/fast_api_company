import streamlit as st
import requests

# Define the FastAPI base URL
BASE_URL = "http://localhost:8000"

st.title("FastAPI Streamlit Menu")

# Menu options
menu = ["Company", "Human", "Parts", "Recruitment"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Company":
    st.subheader("Company")
    st.write("Welcome to Company")

elif choice == "Human":
    st.subheader("Human API")
    human_name = st.text_input("Enter human name")
    human_family = st.text_input("Enter human family")
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/human/create_human", json={"name": human_name, "family": human_family})
        st.write(response.json())

elif choice == "Parts":
    st.subheader("Parts API")
    part_id = st.number_input("Enter part ID", step=1)
    part_name = st.text_input("Enter part name")
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/part/create_part", json={"id": part_id, "part_name": part_name})
        st.write(response.json())

elif choice == "Recruitment":
    st.subheader("Recruitment API")
    human_id = st.number_input("Enter human ID", step=1)
    part_id = st.number_input("Enter part ID", step=1)
    date = st.date_input("Enter date")
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/Recruitment/create_Recruitment", json={"human_id": human_id, "part_id": part_id, "date": date.isoformat()})
        st.write(response.json())

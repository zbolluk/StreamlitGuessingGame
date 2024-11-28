import streamlit as st

# Welcome Page

def Welcome_page():
    st.title("Welcome to the Number Guessing Game! :)")
    st.write("This is a game where you guess a number between 0-100.")
    st.write("Navigate to the **Game** section to play.")
    st.write("Check the **Results** section to see your statistics.")
    st.write("Please, fill out the form!")

    # User Information Form
    with st.form(key="user_form"):
        name = st.text_input("Enter your first name:", placeholder="e.g., John")
        surname = st.text_input("Enter your surname:", placeholder="e.g., Locke")
        age = st.number_input("Enter your age:", min_value=0, max_value=110, step=1)
        occupation = st.text_input("Enter your occupation:", placeholder="e.g., Engineer")

        # Submit Button
        submit_button = st.form_submit_button("Submit")

    # Process Form Data
    if submit_button:
        if name and surname and occupation:
            st.success(f"Welcome, {name} {surname}!")
            st.write(f"**Age:** {age}")
            st.write(f"**Occupation:** {occupation}")
        else:
            st.error("Please fill out all fields.")

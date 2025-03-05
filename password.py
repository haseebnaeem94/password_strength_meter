import streamlit as st
import re


st.markdown(
    """
    <style>
    .stApp {
        background-color: rgb(5, 65, 89); /* Blue background */
        text color: white;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green button */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stTextInput>div>div>input {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        width: 300px; /* Adjust width as needed */
    }
    .strength-indicator {
        height: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .weak {
        background-color: #FF0000; /* Red */
    }
    .medium {
        background-color: #FFA500; /* Orange */
    }
    .strong {
        background-color: #008000; /* Green */
    }
    </style>
    """,
    unsafe_allow_html=True
)


def check_password_strength(password):
    """
    Checks the strength of a given password.

    Args:
        password (str): The password to check.

    Returns:
        tuple: A tuple containing:
            - str: The strength level ("Weak", "Medium", "Strong").
            - str: A message suggesting how to improve the password.
    """
    errors = []
    if len(password) < 8:
        errors.append("Make it at least 8 characters long.")
    if not re.search("[a-z]", password):
        errors.append("Include at least one lowercase letter.")
    if not re.search("[A-Z]", password):
        errors.append("Include at least one uppercase letter.")
    if not re.search("[0-9]", password):
        errors.append("Include at least one digit.")
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Include at least one special character.")

    if len(errors) == 0:
        return "Strong", "Great password!"
    elif len(errors) > 2:
        return "Weak", ", ".join(errors)
    else:
        return "Medium", ", ".join(errors)


st.title("Password Strength Checker")


password_input = st.text_input("Enter your password:", type="password")


if st.button("Check Password Strength"):
   
    strength, message = check_password_strength(password_input)
    st.write(f"**Password Strength:** {strength}")
    st.write(message)
    if strength == "Weak":
        st.markdown('<div class="strength-indicator weak"></div>', unsafe_allow_html=True)
    elif strength == "Medium":
        st.markdown('<div class="strength-indicator medium"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="strength-indicator strong"></div>', unsafe_allow_html=True)




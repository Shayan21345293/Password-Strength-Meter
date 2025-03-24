import streamlit as st
import re
import random
import string

# Set page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔒",
    layout="centered"
)

# Title and description
st.title("Password Strength Checker")
st.markdown("Check how strong your password is or generate a secure one.")

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    max_score = 5
    feedback = []
    
    # Length Check (Basic)
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Good length (8+ characters)")
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    # Extra Length Check (Advanced)
    if len(password) >= 12:
        score += 1
        feedback.append("✅ Excellent length (12+ characters)")
    else:
        feedback.append("❌ Consider using a longer password (12+ characters) for better security")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Good mix of uppercase and lowercase letters")
    else:
        feedback.append("❌ Include both uppercase and lowercase letters")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Includes numbers")
    else:
        feedback.append("❌ Add at least one number (0-9)")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
        feedback.append("✅ Includes special characters")
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*)")
    
    return score, max_score, feedback

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

# Tab 1: Check Password Strength
with tab1:
    password = st.text_input("Enter your password", type="password")
    check_button = st.button("Check Strength")
    
    if check_button and password:
        score, max_score, feedback = check_password_strength(password)
        
        # Display score with progress bar
        st.subheader("Password Score")
        progress_color = "red" if score <= 2 else ("orange" if score <= 4 else "green")
        st.progress(score/max_score)
        st.markdown(f"**Score: {score}/{max_score}**")
        
        # Display strength category
        if score == 5:
            st.success("🔒 Strong Password! Your password meets all criteria.")
        elif score >= 3:
            st.warning("🔓 Moderate Password - Good but missing some security features.")
        else:
            st.error("⚠️ Weak Password - Short, missing key elements.")
        
        # Display feedback
        st.subheader("Feedback")
        for item in feedback:
            st.markdown(item)
    
# Tab 2: Generate Password
with tab2:
    st.subheader("Generate a Strong Password")
    
    # Options for password generation
    length = st.slider("Password Length", 8, 24, 12)
    include_uppercase = st.checkbox("Include Uppercase Letters", value=True)
    include_lowercase = st.checkbox("Include Lowercase Letters", value=True)
    include_numbers = st.checkbox("Include Numbers", value=True)
    include_special = st.checkbox("Include Special Characters", value=True)
    
    if st.button("Generate Password"):
        # Create character pool based on selections
        char_pool = ""
        if include_uppercase:
            char_pool += string.ascii_uppercase
        if include_lowercase:
            char_pool += string.ascii_lowercase
        if include_numbers:
            char_pool += string.digits
        if include_special:
            char_pool += "!@#$%^&*"
        
        if char_pool:  # Check if at least one option is selected
            password = ''.join(random.choice(char_pool) for _ in range(length))
            st.code(password)
            
            # Check strength of generated password
            score, max_score, feedback = check_password_strength(password)
            st.progress(score/max_score)
            st.markdown(f"**Score: {score}/{max_score}**")
        else:
            st.error("Please select at least one character type.")

# Add footer
st.markdown("---")
st.caption("Created by ❤️ Shaya9 Ali") 
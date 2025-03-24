import re
import random
import string

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
    
    # Print all feedback
    for item in feedback:
        print(item)
        
    # Print score
    print(f"\n📊 Password Score: {score}/{max_score}")
    
    # Strength Rating based on user's requirement
    if score == 5:
        print("🔒 Strong Password! Your password meets all criteria.")
    elif score >= 3:
        print("🔓 Moderate Password - Good but missing some security features.")
    else:
        print("⚠️ Weak Password - Short, missing key elements.")
        print(f"🔹 Suggested Strong Password: {generate_strong_password()}")
    
    return score

# User input version
if __name__ == "__main__":
    print("===== Password Strength Checker =====")
    print("1. Check password strength")
    print("2. Generate a strong password")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        password = input("Enter your password to check: ")
        print(f"\nChecking password: {password}")
        check_password_strength(password)
    elif choice == "2":
        strong_password = generate_strong_password()
        print(f"\nGenerated strong password: {strong_password}")
    else:
        print("Invalid choice!") 
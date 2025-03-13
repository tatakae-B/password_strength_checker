import re
import math
import random
import string

def password_entropy(password):
    """Calculate entropy based on character variety and length."""
    char_sets = {
        'lower': r'[a-z]',
        'upper': r'[A-Z]',
        'digits': r'\d',
        'special': r'[^a-zA-Z\d]'
    }
    
    pool_size = sum(bool(re.search(pattern, password)) * len(set(re.findall(pattern, password))) for pattern in char_sets.values())
    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    return entropy

def generate_strong_password(length=12):
    """Generate a strong random password with a mix of character types."""
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

def check_password_strength(password):
    """Evaluate password strength based on regex patterns and entropy."""
    if len(password) < 8:
        return "Weak", "Password too short! Use at least 8 characters.", [generate_strong_password() for _ in range(3)]
    
    entropy = password_entropy(password)
    
    strength = "Weak"
    suggestions = []
    
    if entropy < 28:
        suggestions.append("Use a mix of uppercase, lowercase, digits, and special characters.")
    elif entropy < 50:
        strength = "Moderate"
        suggestions.append("Increase the length for better security.")
    else:
        strength = "Strong"
    
    suggested_passwords = [generate_strong_password() for _ in range(3)] if strength == "Weak" else []
    
    return strength, " ".join(suggestions), suggested_passwords

if __name__ == "__main__":
    password = input("Enter a password: ")
    strength, feedback, suggested_passwords = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")

    if suggested_passwords:
        print("\nSuggested Strong Passwords:")
        for i, pwd in enumerate(suggested_passwords, 1):
            print(f"{i}. {pwd}")
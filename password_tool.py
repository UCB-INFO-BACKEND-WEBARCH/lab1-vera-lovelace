"""
Password Security Tool - INFO 153B/253B Lab 1

Analyze password strength and generate secure passwords.

"""

import string
import random

# Common weak passwords
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley"
]


# ============================================
# TODO 1: Password Strength Checker
# ============================================

def check_password_strength(password):
    """
    Analyze password and return strength score.
    
    Scoring:
    - 8+ characters: 20 points
    - 12+ characters: 30 points (instead of 20)
    - Has number: 20 points
    - Has uppercase: 20 points
    - Has lowercase: 20 points
    - Has special char (!@#$%): 20 points
    - Not in common list: 10 points
    
    Returns:
        dict with keys: "password", "score", "strength", "feedback"
        
    Strength levels:
    - 0-39: "Weak"
    - 40-69: "Medium"
    - 70-100: "Strong"

    Hint: Use .isdigit(), .isupper(), .islower() and string.punctuation
    """
    # TODO: Implement this function

    password = password.strip()
    score = 0
    feedback = []

    # Character type checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()-+."

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Length check
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters.")

    # Character type scoring
    if has_upper:
        score += 20

    if has_lower:
        score += 20

    if has_digit:
        score += 20

    if has_special:
        score += 20

    # Common password check
    if password.lower() not in COMMON_PASSWORDS:
        score += 10


       # Length check
    #if len(password) >= 12:
    #    score += 30
    #elif len(password) >= 8:
    #    score += 20

    # Determine strength level based on score
    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "password": password,
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# ============================================
# TODO 2: Password Generator
# ============================================

def generate_password(length=12, use_special=True):
    """
    Generate a random secure password.

    Requirements:
    - Include uppercase, lowercase, and numbers
    - Include special characters if use_special=True
    - Minimum length: 8

    Args:
        length: Password length (default 12)
        use_special: Include special characters (default True)

    Returns:
        str: Generated password

    Example:
        >>> pwd = generate_password(10, True)
        >>> len(pwd)
        10

    Hint: Use string.ascii_uppercase, string.ascii_lowercase,
          string.digits, and random.choice()
    """
    # TODO: Implement this function
    new_password = []
    new_length = max(8, length)

    all_chars= string.ascii_uppercase + string.ascii_lowercase + string.digits
    if use_special is True:
        all_chars += string.punctuation

    while len(new_password) < new_length:
        new_password.append(random.choice(string.ascii_uppercase))
        new_password.append(random.choice(string.ascii_lowercase))
        new_password.append(random.choice(string.digits))
        new_password.append(random.choice(string.punctuation))
        new_password.append(random.choice(all_chars))
        random.shuffle(new_password)

    #check if password is not common and regenerate if it is
    if ''.join(new_password).lower() in COMMON_PASSWORDS:
        return generate_password(length, use_special)

    # Check character requirements

    check_characters = set(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    if use_special:
        check_characters.update(set(string.punctuation))
    if not any(c in check_characters for c in new_password):
        new_password.append(random.choice(all_chars))


    return ''.join(new_password)


# ============================================
# Simple Testing
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PASSWORD SECURITY TOOL - Quick Test")
    print("=" * 60 + "\n")
    
    # Check if functions are implemented
    try:
        # Test TODO 1
        result = check_password_strength("TestPassword123!")
        
        if result is None:
            print("❌ TODO 1 not implemented yet (returned None)")
            print("\nImplement check_password_strength() and try again.\n")
            exit()
        
        if not isinstance(result, dict):
            print("❌ TODO 1 should return a dictionary")
            exit()
        
        required_keys = ["password", "score", "strength", "feedback"]
        missing_keys = [key for key in required_keys if key not in result]
        
        if missing_keys:
            print(f"❌ TODO 1 missing keys in return dict: {missing_keys}")
            exit()
        
        print("✓ TODO 1 implemented - returns correct structure")
        print(f"  Example: '{result['password']}' → {result['strength']} ({result['score']}/100)")
        
        # Test TODO 2
        pwd = generate_password(12, True)
        
        if pwd is None:
            print("\n❌ TODO 2 not implemented yet (returned None)")
            print("\nImplement generate_password() and try again.\n")
            exit()
        
        if not isinstance(pwd, str):
            print("\n❌ TODO 2 should return a string")
            exit()
        
        print(f"\n✓ TODO 2 implemented - generates passwords")
        print(f"  Example: '{pwd}' (length: {len(pwd)})")
        
        # Success!
        print("\n" + "=" * 60)
        print("✅ Both functions implemented!")
        print("=" * 60)
        print("\nRun the full test suite to verify correctness:")
        print("  python test_password_tool.py")
        print()
        
    except AttributeError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure both functions are defined.\n")
    except Exception as e:
        print(f"❌ Error running functions: {e}")
        print("\nCheck your implementation and try again.\n")
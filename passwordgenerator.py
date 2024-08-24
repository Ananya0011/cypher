import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity level should be 'low', 'medium', or 'high'")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        print("Welcome to Password Generator ")
        print("Made with ❤️ ")
        print("-------------------------------------")
        
        length = int(input("Enter password length: "))
        complexity = input("Enter complexity level (low/medium/high): ").lower()
        
        password = generate_password(length, complexity)
        
        print(f"\nYour generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

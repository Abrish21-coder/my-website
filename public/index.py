import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    """Generates a random password based on user preferences."""
    # Always include lowercase and uppercase letters
    chars = string.ascii_letters  
    
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    # Ensure the password contains at least one of each selected type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase)
    ]
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
        
    # Fill the rest of the password length
    password += [random.choice(chars) for _ in range(length - len(password))]
    
    # Shuffle to make it completely random
    random.shuffle(password)
    
    return "".join(password)

def main():
    print("--- 🔐 Random Password Generator ---")
    try:
        length = int(input("Enter password length (minimum 6): ") or 12)
        if length < 6:
            print("Length too short. Setting to default minimum of 6.")
            length = 6
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    pwd = generate_password(length)
    print(f"\nYour secure password is: {pwd}")
    print("-----------------------------------")

if __name__ == "__main__":
    main()

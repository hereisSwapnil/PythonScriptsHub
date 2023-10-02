import re

def validate_email(email):
    # Define the regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the re.match function to match the pattern against the email address
    if re.match(pattern, email):
        return True
    else:
        return False

# Infinite loop to validate emails based on user input
while True:
    user_input = input("Enter an email address (or type 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    is_valid = validate_email(user_input)
    print(f"Is {user_input} a valid email address? {is_valid}")


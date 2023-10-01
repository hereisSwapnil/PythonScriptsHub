import re

def validate_email(email):
    # Define the regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the re.match function to match the pattern against the email address
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email1 = "user@example.com"
email2 = "invalid-email@.com"
email3 = "another_user@subdomain.example.co.uk"

# Validate the emails
print(f"Is {email1} a valid email address? {validate_email(email1)}")
print(f"Is {email2} a valid email address? {validate_email(email2)}")
print(f"Is {email3} a valid email address? {validate_email(email3)}")

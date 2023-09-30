def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    contains_upper = any(char.isupper() for char in password)
    contains_lower = any(char.islower() for char in password)
    contains_digit = any(char.isdigit() for char in password)
    contains_special = any(char in "!@#$%^&*()-_+=<>?/:;,." for char in password)

    # Evaluate criteria
    strength = 0
    if length_criteria:
        strength += 1
    if contains_upper:
        strength += 1
    if contains_lower:
        strength += 1
    if contains_digit:
        strength += 1
    if contains_special:
        strength += 1

    return strength

def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)

    if strength == 5:
        print("Password is very strong!")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is moderate.")
    elif strength >= 1:
        print("Password is weak.")
    else:
        print("Password does not meet minimum criteria.")

if __name__ == "__main__":
    main()

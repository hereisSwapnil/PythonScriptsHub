import random

def roll_die():
    result = random.randint(1, 6)
    return result

def main():
    print("Welcome to the six-sided die roller!")

    while True:
        input("Press Enter to roll the die...")
        result = roll_die()
        print(f"You rolled a {result}!")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for using the die roller!")

if __name__ == "__main__":
    main()

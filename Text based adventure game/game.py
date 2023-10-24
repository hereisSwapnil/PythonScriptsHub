def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious forest. You have to make decisions to find your way out.")
    print("Let the adventure begin!\n")


def make_choice(choices):
    print("Available Choices:")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def forest():
    print("\nYou are in a dense forest. You can hear mysterious sounds all around you.")
    choices = ["Go deeper into the forest", "Try to climb a tree", "Go back"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou venture deeper into the forest and get lost.")
        print("Game Over! You are lost in the forest.")
    elif choice == 2:
        print("\nYou climb a tree and spot a river in the distance.")
        river()
    else:
        print("\nYou decide to go back and find a different path.")
        start()


def river():
    print("\nYou reach the riverbank. The river is fast-flowing and looks dangerous.")
    choices = ["Swim across the river", "Look for a bridge", "Go back to the forest"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou attempt to swim across the river but get swept away by the current.")
        print("Game Over! You got drowned in the river.")
    elif choice == 2:
        print("\nYou find a sturdy bridge and safely cross the river.")
        treasure()
    else:
        print("\nYou decide to go back to the forest and explore other options.")
        forest()


def treasure():
    print("\nCongratulations! You have successfully crossed the river.")
    print("You discover a hidden treasure chest!")
    print("You have won the game! Well done, adventurer!")


def start():
    introduction()
    forest()


if __name__ == "_main_":
    start()
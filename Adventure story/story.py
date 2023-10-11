import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("You must make choices to find your way out.")
    time.sleep(1)

def forest_path():
    print("\nYou are on a forest path. You see a fork in the road.")
    print("Do you want to go left or right, or explore a nearby cave?")
    choice = input("Type 'left', 'right', or 'cave': ").lower()
    
    if choice == "left":
        print("You chose to go left.")
        time.sleep(1)
        waterfall()
    elif choice == "right":
        print("You chose to go right.")
        time.sleep(1)
        bridge()
    elif choice == "cave":
        print("You decided to explore the cave.")
        time.sleep(1)
        cave()
    else:
        print("Invalid choice. Please enter 'left', 'right', or 'cave'.")
        forest_path()

def waterfall():
    print("\nYou arrive at a beautiful waterfall surrounded by lush vegetation.")
    time.sleep(1)
    print("You can take a swim or continue your journey.")
    choice = input("Type 'swim' or 'continue': ").lower()

    if choice == "swim":
        print("You take a refreshing swim and feel rejuvenated.")
        time.sleep(1)
        print("You continue your journey.")
        forest_path()
    elif choice == "continue":
        print("You decide to continue your journey without taking a swim.")
        forest_path()
    else:
        print("Invalid choice. Please enter 'swim' or 'continue'.")
        waterfall()

def bridge():
    print("\nYou arrive at a rickety old bridge hanging over a deep chasm.")
    time.sleep(1)
    print("Do you want to cross the bridge or turn back?")
    choice = input("Type 'cross' or 'turn back': ").lower()

    if choice == "cross":
        print("You take a deep breath and start crossing the bridge.")
        time.sleep(1)
        print("The bridge creaks but holds, and you make it to the other side.")
        time.sleep(1)
        dragon()
    elif choice == "turn back":
        print("You decide not to risk it and turn back to the forest path.")
        forest_path()
    else:
        print("Invalid choice. Please enter 'cross' or 'turn back'.")
        bridge()

def dragon():
    print("\nAs you continue, you stumble upon a sleeping dragon!")
    time.sleep(1)
    print("You can either sneak past the dragon or try to wake it up.")
    choice = input("Type 'sneak' or 'wake up': ").lower()

    if choice == "sneak":
        print("You manage to sneak past the dragon without waking it.")
        time.sleep(1)
        treasure()
    elif choice == "wake up":
        print("You try to wake up the dragon, but it opens its eyes!")
        time.sleep(1)
        print("In a moment of panic, you run away.")
        time.sleep(1)
        forest_path()
    else:
        print("Invalid choice. Please enter 'sneak' or 'wake up'.")
        dragon()

def cave():
    print("\nYou enter a dark cave. It's very cold inside.")
    time.sleep(1)
    print("You find a chest. Do you want to open it or leave?")
    choice = input("Type 'open' or 'leave': ").lower()

    if choice == "open":
        print("You open the chest and find a valuable gem!")
        time.sleep(1)
        print("You can sell it and become rich.")
        end_game("win")
    elif choice == "leave":
        print("You leave the chest and continue your journey.")
        forest_path()
    else:
        print("Invalid choice. Please enter 'open' or 'leave'.")
        cave()

def treasure():
    print("\nYou find yourself in a hidden grove with a magnificent treasure chest!")
    time.sleep(1)
    print("Do you want to open the treasure chest or leave it alone?")
    choice = input("Type 'open' or 'leave': ").lower()

    if choice == "open":
        print("You open the treasure chest and discover it's full of gold and jewels!")
        time.sleep(1)
        print("You have found the ultimate treasure!")
        end_game("win")
    elif choice == "leave":
        print("You decide to leave the treasure chest untouched and continue your journey.")
        forest_path()
    else:
        print("Invalid choice. Please enter 'open' or 'leave'.")
        treasure()

def end_game(result):
    if result == "win":
        print("\nCongratulations! You found the treasure and became rich. You win!")
    else:
        print("\nOh no! You encountered a mishap and couldn't find your way out. You lose!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        start_game()
    else:
        print("Thanks for playing!")

def start_game():
    introduction()
    forest_path()

start_game()

# #program to make a game of rock, papers & scissors using python
# import random

# maxScore=int(input("Enter the Max Score: "))
# compScore=0
# userScore=0

# while maxScore:
#     user_input=input("Choose (rock (r), paper (p) or scissors (s): ")
#     options=["r","p","s"]
#     computer_input=random.choice(options)
#     print("Your Choice: ", user_input, "\nComputer's Choice: ", computer_input)

#     if (user_input==computer_input):
#         print("It's a TIE! Nobody gets a score!\n")
#     elif (user_input=="r"):
#         if (computer_input=="p"):
#             print("Computer WON! You Lose!\n")
#             compScore+=1
#         else:
#             print("You WON! Computer Lose!\n")
#             userScore+=1
#     elif (user_input=="p"):
#         if (computer_input=="s"):
#             print("Computer WON! You Lose!\n")
#             compScore+=1
#         else:
#             print("You WON! Computer Lose!\n")
#             userScore+=1
#     elif (user_input=="s"):
#         if (computer_input=="r"):
#             print("Computer WON! You Lose!\n")
#             compScore+=1
#         else:
#             print("You WON! Computer Lose!\n")
#             userScore+=1
#     print("User Score: ", userScore, "\nComputer Score: ", compScore)

#     if (userScore==maxScore):
#         print("User WON!")
#     elif (compScore==maxScore):
#         print("Computer WON!")
#     if (userScore==maxScore or compScore==maxScore):
#         break

import random

def get_user_choice():
    while True:
        user_input = input("Choose (rock (r), paper (p), or scissors (s)): ").lower()
        if user_input in ['r', 'p', 's']:
            return user_input
        else:
            print("Invalid input. Please choose 'r', 'p', or 's'.")

def determine_winner(user_choice, computer_choice):
    outcomes = {'r': 's', 's': 'p', 'p': 'r'}
    if user_choice == computer_choice:
        return "It's a tie!", None
    elif outcomes[user_choice] == computer_choice:
        return "You win!", 'user'
    else:
        return "Computer wins!", 'computer'

def play_game():
    max_score = int(input("Enter the Max Score: "))
    comp_score = 0
    user_score = 0

    while True:
        user_input = get_user_choice()
        options = ['r', 'p', 's']
        computer_input = random.choice(options)

        print("Your Choice:", user_input)
        print("Computer's Choice:", computer_input)

        result, winner = determine_winner(user_input, computer_input)
        print(result)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            comp_score += 1

        print("User Score:", user_score)
        print("Computer Score:", comp_score)

        if user_score == max_score:
            print("User WON!")
            break
        elif comp_score == max_score:
            print("Computer WON!")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == 'yes'

while True:
    if not play_game():
        print("Thanks for playing! Goodbye.")
        break

#program to make a game of rock, papers & scissors using python
import random

maxScore=int(input("Enter the Max Score: "))
compScore=0
userScore=0

while maxScore:
    user_input=input("Choose (rock (r), paper (p) or scissors (s): ")
    options=["r","p","s"]
    computer_input=random.choice(options)
    print("Your Choice: ", user_input, "\nComputer's Choice: ", computer_input)

    if (user_input==computer_input):
        print("It's a TIE! Nobody gets a score!\n")
    elif (user_input=="r"):
        if (computer_input=="p"):
            print("Computer WON! You Lose!\n")
            compScore+=1
        else:
            print("You WON! Computer Lose!\n")
            userScore+=1
    elif (user_input=="p"):
        if (computer_input=="s"):
            print("Computer WON! You Lose!\n")
            compScore+=1
        else:
            print("You WON! Computer Lose!\n")
            userScore+=1
    elif (user_input=="s"):
        if (computer_input=="r"):
            print("Computer WON! You Lose!\n")
            compScore+=1
        else:
            print("You WON! Computer Lose!\n")
            userScore+=1
    print("User Score: ", userScore, "\nComputer Score: ", compScore)

    if (userScore==maxScore):
        print("User WON!")
    elif (compScore==maxScore):
        print("Computer WON!")
    if (userScore==maxScore or compScore==maxScore):
        break
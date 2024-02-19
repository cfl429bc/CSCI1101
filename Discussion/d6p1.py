# imports random
import random

# greets the player
print("Let's play rock, paper, scissors!")

# sets initial values
again = "y"
choices = ["rock", "paper", "scissors"]

# while user wants yo play again
while again == "y":
    user = str(input("What do you pick? "))
    computer = random.choice(choices)
    if user not in choices:
        print("Only rock, paper, and scissors are valid!")
    else:
        print(f"Game choses {computer}")
        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") and (user == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("The game wins!")
    
    again = str(input("Play again (y/n)?"))
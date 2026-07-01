#ROCK PAPER SCISSORS GAME
import random # it is best to do such at start
print("Hello Welcome to this game!")
print("The Pattern of Game is a Rock,Scissors and a Paper !")
user_score=0
computer_score=0
round_number=0
#Rules
print("Rule no 1 is:Rock beats Scissors")
print("Rule no 2 is:Scissors beats Paper")
print("Rule no 3 is:Paper beats Rock")
# now go towards the main
while True:
    round_number+=1
    print(f"Round {round_number}")
    options=["rock","paper","scissors"]
    user_choice=input('Enter your choice between "rock","paper",and "scissors" :').lower()
    # this will import things here
    computer_choice=random.choice(options)# here computer will choose from options
    if user_choice == computer_choice:
        print("Game is drawn")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    elif (computer_choice == "rock" and user_choice == "scissors") or \
         (computer_choice == "scissors" and user_choice == "paper") or \
         (computer_choice == "paper" and user_choice == "rock"):
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("Invalid input! Please type rock, paper, or scissors.")
        continue  # repeat the round if invalid
# here we will simply display result
    print("User chose:", user_choice)
    print("Computer chose:",computer_choice)
    #here we will also print the current score
    print(f"Score You:{user_score}|Computer:{computer_score}") # pip symbol used between them 
    # ask user to play again
    play_again=input("Do you want to play this game again(yes/no):")
    if play_again!="yes":
        print(f"Final score You :{user_score}|Computer :{computer_score}")
        print("thanks for playing this game bro!good by ")
        break







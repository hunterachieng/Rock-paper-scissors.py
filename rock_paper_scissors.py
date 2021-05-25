
import random
while True:
    #to begin from the top everytime player agrees to continue
 player_input = input ("What is your choice ('rock', 'paper', 'scissors'): \n")
 computer = random.choice(["rock", "paper", "scissors"])
# r > s ,s > p , p > r 

 if player_input == computer:
  print(f"Its a tie! You chose {player_input} and computer chose {computer}") 
 elif player_input == "rock":
    if computer == "scissors":
        print("Rock smashes scissors.You win!")
    else:
        print("Paper covers rock.Computer wins!")
 elif player_input == "scissors":
    if computer == "paper":
        print("Scissors cuts paper.You win!")
    else:
        print("Rock smashes scissors. Computer wins!")
 elif player_input == "paper":
    if computer == "rock":
        print( "Paper covers rock. You win!")
    else:
        print("Scissors cut paper. Computer wins!")
 try_again = input("Want to play again? ('y'/'n'): \n").lower()
 if try_again == "n":
    break

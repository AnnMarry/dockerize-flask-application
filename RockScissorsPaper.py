import random

def user_choice():
# user picks thing
  valid_choice = False
  while valid_choice != True:
    player_choice = input("Choose rock, paper, scissors : ")
    if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
      valid_choice = True
      break
    print("Please pick a valid word!")
  return player_choice

def cp_choice():
   # computer picks thing
  computer_choice = random.randint(1,3)
  if computer_choice == 1:
    computer_choice = "rock"
  if computer_choice == 2:
      computer_choice = "scissors"
  else:
    computer_choice = "paper"
  return computer_choice

def comparisons(player_choice, computer_choice, player_score, computer_score):
    # Player chooses rock
  if player_choice == "rock" and computer_choice == "rock":
    print("Tie, try again!\n")
  elif player_choice == "rock" and computer_choice == "scissors":
    print("You win, rock smash scissors!\n")
    player_score += 1
  elif player_choice == "rock" and computer_choice == "paper":
    print("You lose, paper covers rock!\n")
    computer_score += 1

    # Player chooses scissors
  if player_choice == "scissors" and computer_choice == "scissors":
     print("Tie, try again!\n")
  elif player_choice == "scissors" and computer_choice == "paper":
    print("You win, scissors beats paper!\n")
    player_score += 1
  elif player_choice == "scissors" and computer_choice == "Rock":
    print("You lose, rock beats scissors\n")
    computer_score += 1


    # Player chooses paper
  if player_choice == "paper" and computer_choice == "paper":
    print("Tie, try again!\n")
  elif player_choice == "paper" and computer_choice == "rock":
    print("You win, paper beats rock!\n")
    player_score += 1
  elif player_choice == "paper" and computer_choice == "scissors":
    print("You lose, scissors beats paper\n")
    computer_score += 1

  

def check_win(player_score, computer_score, running):
  if computer_score == 3:
    print("Tough luck, computer wins!")
    running = False
  elif  player_score == 3:
    print("Well done, you win!")
    running = False
  else:
    running = True

  return player_score, computer_score, running

# variables
player_score = 0
computer_score = 0

running = True
while running == True:

  # Player chooses rock, paper or scissors
  player_choice = user_choice()

  # Computer chooses rock, paper or scissors 
  computer_choice = cp_choice()

  # comparison of player and computer choices  
  comparisons(player_choice, computer_choice, player_score, computer_score)

  check_win(player_score, computer_score, running)

print("End of game")
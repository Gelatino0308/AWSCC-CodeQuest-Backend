import random

print("=== Welcome to the Rock-Paper-Scissors Game! ===\n")
print("[Play against the computer by entering your choice (Rock, Paper, or Scissors)]")
print("[Be careful of spelling mistakes!]\n")

player = input("Player's choice: ").lower()

pick_list = ["rock", "paper", "scissors"]
computer = random.choice(pick_list)
print(f"Computer's choice: {computer}")
    
if (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
    print("\n>> You WIN!")
elif (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
    print("\n>> Computer WINS =(")
else:
    print("\n>> It's a DRAW!")

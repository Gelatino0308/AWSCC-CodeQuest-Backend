print("=== Welcome to the Rock-Paper-Scissors Game! ===\n")
print("[Enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors]")

player1 = input("Player 1: ")
player2 = input("Player 2: ")
    
if (player1 == 'R' and player2 == 'S') or (player1 == 'P' and player2 == 'R') or (player1 == 'S' and player2 == 'P'):
    print("\nPlayer1 WINS!")
elif (player2 == 'R' and player1 == 'S') or (player2 == 'P' and player1 == 'R') or (player2 == 'S' and player1 == 'P'):
    print("\nPlayer2 WINS!")
else:
    print("\nIt's a DRAW!")

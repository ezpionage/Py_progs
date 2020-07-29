import random
player_1 = input("rock, paper, scissors?").lower()
print("No Cheating! \n" * 20)
player_2 = random.choice(["rock","paper","scissors"]).lower()

print(f"Player 2 plays {player_2}")

if player_1 == player_2:
	print("It's a tie!")
elif player_1 == "rock":
	if player_2 == "scissors":
		print("Player 1 wins the game!")
	else:
		print("Player 2 wins the game!")
elif player_1 == "paper":
	if player_2 == "scissors":
		print("Player 2 wins the game!")
	else:
		print("Player 1 wins the game!")
elif player_1 == "scissors":
	if player_2 == "rock":
		print("Player 2 wins the game!")
	else:
		print("Player 1 wins the game!")
else:
	print("Something went wrong!")
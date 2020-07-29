import random
player_1_wins = 0
player_2_wins = 0
winning_score = 3

while player_1_wins < winning_score and player_2_wins < winning_score:
	print(f"Player score:{player_1_wins} Player 2 score:{player_2_wins}")
	print("...rock...")
	print("...paper...")
	print("...scissors...")

	player_1 = input("rock, paper, scissors? ").lower()
	player_2 = random.choice(["rock","paper","scissors"]).lower()

	print(f"Player 1 plays - {player_1}")
	print(f"Player 2 plays - {player_2}")

	if player_1 == "quit" or player_1 == "q":
		break
	if player_1 == player_2:
		print("It's a tie!")
	elif player_1 == "rock":
		if player_2 == "scissors":
			print("Player 1 wins the game!")
			player_1_wins += 1
		else:
			print("Player 2 wins the game!")
			player_2_wins += 1
	elif player_1 == "paper":
		if player_2 == "scissors":
			print("Player 2 wins the game!")
			player_2_wins += 1
		else:
			print("Player 1 wins the game!")
			player_1_wins += 1
	elif player_1 == "scissors":
		if player_2 == "rock":
			print("Player 2 wins the game!")
			player_2_wins += 1
		else:
			print("Player 1 wins the game!")
			player_1_wins += 1
	else:
		print(f"Player score:{player_1_wins} Player 2 score:{player_2_wins}")

if player_1_wins > player_2_wins:
	print("Congrats, you have won!")
elif player_2_wins == player_1_wins:
	print("It's a tie!")
else:
	print("Oh No :( Player 2 wins!")
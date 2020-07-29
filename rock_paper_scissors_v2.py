player_1 = input("Rock, Paper, Scissors?")
print("No Cheating! \n" * 20)
player_2 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRock, Paper, Scissors?")

if player_1 == player_2:
	print("It's a tie!")
elif player_1 == "Rock":
	if player_2 == "Scissors":
		print("Player 1 wins the game!")
	elif player_2 == "Paper":
		print("Player 2 wins the game!")
elif player_1 == "Paper":
	if player_2 == "Scissors":
		print("Player 2 wins the game!")
	elif player_2 == "Rock":
		print("Player 1 wins the game!")
elif player_1 == "Scissors":
	if player_2 == "Rock":
		print("Player 2 wins the game!")
	if player_2 == "Paper":
		print("Player 1 wins the game!")
else:
	print("Something went wrong!")
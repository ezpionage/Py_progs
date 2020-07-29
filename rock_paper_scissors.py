player_1 = input("Rock, Paper, Scissors?")
player_2 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRock, Paper, Scissors?")


if player_1 == "Rock" and player_2 == "Scissors":
	print ("Player 1 wins the game!")
elif player_1 == "Scissors" and player_2 == "Paper":
	print ("Player 1 wins the game!")
elif player_1 == "Paper" and player_2 == "Rock":
	print ("Player 1 wins the game!")
elif player_2 == "Rock" and player_1 == "Scissors":
	print ("Player 2 wins the game!")
elif player_2 == "Scissors" and player_1 == "Paper":
	print ("Player 2 wins the game!")
elif player_2 == "Paper" and player_1 == "Rock":
	print ("Player 2 wins the game!")
elif player_1 == player_2:
	print ("It's a tie"!)
else:
	print ("Wrong command, try again!")
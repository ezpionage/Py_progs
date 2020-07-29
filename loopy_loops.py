from random import randint  # use randint(a, b) to generate a random number between a and b
 
random_number = randint(1,10)

user_guess = " "


while user_guess != random_number:
	user_guess = input("Guess the number 1 to 10? ")
	user_guess = int(user_guess)
	if user_guess < random_number:
		print("Too Low")
	elif user_guess > random_number:
		print("Too High")
	else:
		print("That's the winning number!")
		play_again = input("Do you want to play again? y/n ")
		if play_again == "y":
			random_number = randint(1,10)
			user_guess = None
		else:
			print("Thanks for playing!")
			break

print(random_number)

#for loop in range(1,21):
#		if loop == 4 or loop == 13:
#			print(f"{loop} that's unlucky")
#		elif loop % 2 == 0:
#			print(f"{loop} is odd")
#		else:
#			print(f"{loop} is even")

for loop in range(1,21):
		if loop == 4 or loop == 13:
			state = "Unlucky"
		elif loop % 2 == 0:
			state = "Even"
		else:
			state = "Odd"
		print(f"{loop} that's {state}")
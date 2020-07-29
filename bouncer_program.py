# This is a program to ask your age
age = input("Enter your age: ")
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print ("Green Wristband. Entry to the 18 club")
	elif age >= 21:
		print ("Red Wristband. Welcome to the 21 club")
	elif age < 18:
		print ("Sorry, you're too young")

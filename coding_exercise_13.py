# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for loop in range(10,21):
    if loop % 2 != 0:
    	x = loop + x
    	print(x)

print(x)

o = 1

for loopie in range(30,45):
	if loopie % 2 != 0:
		o = loopie + o
		print(o)

print(o)

print(x * o)

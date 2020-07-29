#for x in range(3):
#	for num in range(1,11):
#		print("*" * num)

#num = "*"
#count = 1

	#while count < 11:
		#print(num * count)
		#count += 1

#num = " "
#count = 1

#while count < 20:
#		print(num * count)
#		count % 2 != 0
#		count += 2
#		num = 1 + "*"

num = int(input("How many Row's do you want"))
for i in range(0,num):
	for j in range(0,num-i-1):
		print(end=" ")
	for j in range(0,i+1):
		print("*",end=" ")
	print()

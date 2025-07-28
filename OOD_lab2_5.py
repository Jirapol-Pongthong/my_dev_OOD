def bon(w):
	a = 0
	sum = set()
	for i in range(len(w)):
		for j in range(i + 1, len(w)):
			if j < len(w) and w[i] == w[j]:
				sum.add(w[i])
				break
	for i in sum:
		a += ord(i)-96
	
	a = a * 4
	return a 

			
secretCode = input("Enter secret code : ")
print(bon(secretCode))
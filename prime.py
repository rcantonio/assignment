'''
Prime numbers from 1-100
'''

def isPrime(number):
	for i in range(2, number):
		if not number % i:
			return False
	return True

for j in range (2, 101):
	if isPrime(j):
		print(j, "is a prime number")

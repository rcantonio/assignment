'''
Prime numbers from 1-100
'''

def isPrime(number):
	for x in range(2,101):
		if not number % x and x != number:
			return False
	return True

for a in range (2,101):
	if isPrime(a):
		print(a, "is a prime number")

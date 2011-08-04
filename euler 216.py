import math
count=0
def isprime(n):
	for i in range(2,math.ceil(math.sqrt(n))+1):
		if not n%i:
			return False
	return True

for i in range(2,50000001):
	if isprime(2*i**2-1):
		count+=1

def maxPrime(n):
	if n <=2:
		return n
	i = n
	j = 2
	while i != j:
		i-=1
		prime = True 
		for j in range(2,i):
			print('i = ',i)
			print('j = ',j)
			if i%j:
				prime = False
				continue
		if prime:
			return i
	return i

if __name__ == '__main__':
	print (maxPrime(8))

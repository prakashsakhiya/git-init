def power(n): 
	if n==1: 
		return 2
	return 2*power(n-1) 

n =4
print(power(n)) 
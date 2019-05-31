def staircase(n):
	if n > 0 and n <= 100:
		for stair in range (1,n+1):
			#print(stair)
			#print(n-stair)
			print(' '*(n-stair) + '#'*stair)
			
staircase(10)
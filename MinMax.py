def miniMaxSum(arr):
	if len(arr) == 5:
		print('{} {}'.format(sum([min_val for min_val in arr if min_val<max(arr)]), sum([max_val for max_val in arr if max_val > min(arr)])))

miniMaxSum([1,3,5,7,9])
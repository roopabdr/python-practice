#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below
def miniMaxSum(arr):
	if len(arr) == 5 and min(arr) != max(arr):
		print('{} {}'
		.format(
			sum([min_val for i, min_val in enumerate(arr) if (min_val < max(arr) and i < len(arr)-1) or (min_val==max(arr) and i <= len(arr)-2)])
			,sum([max_val for j, max_val in enumerate(arr) if (max_val > min(arr) and j < len(arr)-1) or (max_val==max(arr) and j <= len(arr)-2)])
			)
		)
	# elif len(arr) == 5 and min(arr) == max(arr):
	# 	arr.pop()
	# 	print('{} {}'.format(sum(arr), sum(arr)))

if __name__ == '__main__':
	# arr = list(map(int, input().rstrip().split()))
	# miniMaxSum(arr)
	miniMaxSum([1,5,5,5,5])
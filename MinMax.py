#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below
def miniMaxSum(arr):
	if len(arr) == 5 and min(arr) != max(arr):
		print('{} {}'.format(sum([min_val for min_val in arr if min_val<max(arr)]), sum([max_val for max_val in arr if max_val > min(arr)])))
	elif len(arr) == 5 and min(arr) == max(arr):
		arr.pop()
		print('{} {}'.format(sum(arr), sum(arr)))

if __name__ == '__main__':
	arr = list(map(int, input().rstrip().split()))
	miniMaxSum(arr)
	#miniMaxSum([5,5,5,5,5])
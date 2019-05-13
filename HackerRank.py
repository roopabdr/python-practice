from __future__ import division
input = [6,-4,3,-9,0,4]

def plusMinus(arr):
		arr_len = len(arr)
		if arr_len > 0 and arr_len <=100:
			positive = [p for p in arr if p>0]
			print("{:.{}f}".format(len(positive)/arr_len, 6))
			negative = [n for n in arr if n<0]
			print("{:.{}f}".format(len(negative)/arr_len, 6))
			zeroes = [zero for zero in arr if zero ==0]
			print("{:.{}f}".format(len(zeroes)/arr_len,6))
			
plusMinus(input)
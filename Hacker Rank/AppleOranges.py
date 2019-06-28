def countApplesAndOranges(s, t, a, b, apples, oranges):
	for index, apple in enumerate(apples):
		apples[index] = apple + a
	for index, orange in enumerate(oranges):
		oranges[index] = orange + b
	apple_count = len([apple for apple in apples if apple >= s and apple<=t])
	orange_count = len([orange for orange in oranges if orange >= s and orange<=t])
	print(apple_count)
	print(orange_count)
	
countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
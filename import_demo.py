import other_script as os

scores = [88,92,79,93,85]

mean = os.mean(scores)
curved = os.add_five(scores)

mean_c = os.mean(curved)

print('Scores: ', scores)
print('Original Mean:', mean, " New Mean:", mean_c)

print(__name__)
print(os.__name__)
from itertools import permutations

perm = permutations([1,2,3,4,5,6,7,8,9], 2)

summation = [sum(add) for add in list(perm)]

print(summation)


num = [15, 14, 16]

k = 3
tens = [3, 2, 2]
perm = permutations([1,7,4], 2)

summation = [sum(add) for add in list(perm)]

print(summation)
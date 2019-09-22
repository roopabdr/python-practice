def kangaroo(x1, v1, x2, v2):
    print((x2 - x1), (v1 - v2))
    if (v1 - v2) != 0:
        z1 = (x2 - x1) % (v1 - v2)
        z2 = (x2 - x1) / (v1 - v2)
        return 'YES' if z1 == 0 and z2 > 0 else 'NO'
    return 'NO'


# print(kangaroo(21,6,47,3))
# print(kangaroo(0,2,5,3))
print(kangaroo(43,2,70,2))
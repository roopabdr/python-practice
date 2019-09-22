def extraLongFactorials(n):
    value = [num for num in range(1, n)]
    value.append(n)    
    result = 1
    for num in value:
        result *= num
    print(result)
    return result

extraLongFactorials(25)
def birthdayCakeCandles(ar):
    age = len(ar)
    tallest = max(ar)
    count = 0
    if age >=1 and age <= 10**5:
        count = len([candle for candle in ar if candle == tallest])
    return count

print(birthdayCakeCandles([3,3,1,4]))
# print(birthdayCakeCandles())

# with open('./BirthdayCake Input.txt') as f:
#     array = str(f.read()).split(',')
#     print(birthdayCakeCandles([array]))
#     print(array)
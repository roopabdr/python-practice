# name = input('Enter a name: ')
# print('Hello',name)

# num = input('Enter a number: ')
# num += 2
# print(num) # errors

# num = int(input('Enter a number: '))
# num += 2
# print(num) # works

# num = int(input('Enter a number: '))
# num += 2
# print(num) # errors if input is a float like 2.5

# num = float(input('Enter a number: '))
# num += 2
# print(num) # works if entering a float value although int can be difficult now

# num = int(float(input('Enter a number: ')))
# num += 2
# print(num) # works for both int and float now but now converts the result into an absolute integer stripping off the decimal places

# x = eval(input('Enter an expression: '))
# print(x)

#eval with variables
num = 30
x = eval('num + 42')
print(x)
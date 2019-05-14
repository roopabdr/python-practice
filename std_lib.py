# print e to the power of 3 using the math module
# import math

# def expo(num):
#     print(math.exp(num))


# expo(3)

# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    rand_words = []
    for rand in range(3):
        # print('len word_list',len(word_list))
        index = random.randint(0, len(word_list)-1)
        # print('index',index)
        rand_words.append(word_list[index])
    
    return "".join(rand_words)
    # alternative one line solution to above code: return ''.join(random.sample(word_list,3))


# test your function
print(generate_password())
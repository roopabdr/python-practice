# normal read operation
# f = open('./basic.txt','r')
# file_data = f.read()
# print(file_data)
# f.close()

#normal write operation
# f = open('./another_file.txt','w')
# f.write('Hello World!')
# f.close()


# error reading too many files
# files = []
# for i in range(10000):
#     files.append(open('./another_file.txt', 'r'))
#     print(i)


# ways to auto close the file handle without having to call f.close() method
# with open('./another_file.txt', 'r') as f:
#     file_data = f.read()

# print(file_data)


# reading upto few positions and then again continuing from there
# this is done by passing integer arguments to the read function
# with open('./basic.txt') as song:
#     print(song.read(2))
#     print(song.read(8)) # picks of from third character automatically
#     print(song.read()) # picks of from 11th (after reading 2+8 chars) character automatically

# array of file read lines
mary_lines = []
with open('./basic.txt') as f:
    for line in f:
        mary_lines.append(line.strip()) # strips off \n character from the the newline while reading a file

print(mary_lines)


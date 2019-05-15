# Write your code here
flower_dict = {}
# HINT: create a dictionary from flowers.txt
with open("./flowers.txt") as f:
    for line in f:
        key_dict = str(line.strip().split(":")[0])
        value_dict = str(line.strip().split(":")[1]).strip()
        flower_dict.update({key_dict: value_dict})
        # print(line.strip())
# HINT: create a function to ask for user's first and last name
def user_input():
    full_name = input("Enter your First [space] Last name only: ")
    return full_name[:1]

def main():
    first_letter = user_input()
    # result = ''.join([flower for letter, flower in flower_dict.items() if letter == first_letter])
    result = flower_dict[first_letter] # Best and easy way to query - no need of looping through and checking for it
    print(result)

# print the desired output
if __name__ == "__main__":
    main()
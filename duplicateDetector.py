
userInput = input("Enter your text: ")

my_list = [char for char in userInput]
duplicate = set([x for x in my_list if my_list.count(x) > 1])
print(duplicate)


#first code commit

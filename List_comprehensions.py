
#List Comprehension

my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num*2 for num in range(1, 100)]
my_list3 = [num*2 for num in range(1, 100) if num % 2 == 0]
print(my_list3)
#print(list(map(lambda item: item *2, my_list2)))

#Set Comprehension
my_list = {char for char in 'hello'}
print(my_list)

my_list2 = {num*2 for num in range(1, 100)}
my_list3 = {num*2 for num in range(1, 100) if num % 2 == 0}
print(my_list3)

#Dictionary Comprehension
some_list = [char for char in 'hello']
duplicate = set([x for x in some_list if some_list.count(x) > 1])
print(duplicate)
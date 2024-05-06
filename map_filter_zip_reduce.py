
# def multiply_by2(item):
#     return item *2

# def only_odd(item):
#     return item % 2 != 0

# print(list(map(multiply_by2, [1,2,3])))

# print(list(filter(only_odd, [1,2,3])))

# print(list(zip([1,2,3], [10, 20, 30])))

#1 Capitalize all of the pet names and print the list


my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(item):
    return item.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def benchmark(item):
    return item >= 50

print(list(filter(benchmark, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
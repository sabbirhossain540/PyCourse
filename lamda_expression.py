

#Structure lamda param: action, data
# print(list(map(lambda item: item*2, [1,2,3])))
# print(list(filter(lambda item: item >= 40, [4,56.2,543,55,3])))

my_list = [5,4,3]
print(list(map(lambda item: item*item, my_list)))

#Shorting based on first 
a = [(0,2), (4,3), (1,0), (5,4), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

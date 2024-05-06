# #decorator pattern
# def my_decorator(func):
#     def warp_function(*args, **kwargs):
#         print("***********")
#         func(*args, **kwargs)
#         print("***********")
#     return warp_function


# @my_decorator
# def hello(gretting, emoji=':()'):
#     print(gretting, emoji)


# hello("Assalamu Alaikum")

from time import time
def performance(fn):
    def warper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result
    return warper

@performance
def long_time():
    for i in range(1, 1000000):
        i*5


print(long_time())
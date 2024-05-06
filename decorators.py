#decorator pattern
def my_decorator(func):
    def warp_function(*args, **kwargs):
        print("***********")
        func(*args, **kwargs)
        print("***********")
    return warp_function


@my_decorator
def hello(gretting, emoji=':()'):
    print(gretting, emoji)


hello("Assalamu Alaikum")
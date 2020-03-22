from time import time

print('---------------------------DECORATORS--------------------------------')


def hello():
    return 'Hello!'


greet = hello
del hello
# hello() # ! Error
print("greet():", greet())  # Hello!


def hello2(func):
    return func()


def greet2():
    return 'Still here!'


a = hello2(greet2)
print("a:", a)  # Still here!

print('---------------------------HIGHER ORDER FUNCTION----------------------')
# * HOC - The function that accept other function as parameter
# * or return function as result


print('---------------------------DECORATOR 2--------------------------------')


def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorator
def hello3():
    print('Hello!')


print("hello3():", hello3())  # ******* Hello! *********, None


print('---------------------------DECORATOR 3--------------------------------')


# * Decorator pattern
def my_decorator4(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func


@my_decorator4
def hello4(greeting, emoji=':('):
    print(greeting, emoji)


# ******* Custom hello! :( *********, None
print("hello4('Custom hello!'):", hello4('Custom hello!'))


print('---------------------------DECORATOR 4--------------------------------')


def performance(fn):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = fn(*args, **kwargs)
        time2 = time()
        print(f'took {time2 - time1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


print("long_time():", long_time())  # * took 0.008205175399780273 ms
print(":", )  #

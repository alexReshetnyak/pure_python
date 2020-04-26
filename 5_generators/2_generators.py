from time import time
print('---------------------------GENERATORS--------------------')


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
    print('1')
    for i in range(1000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5


print("long_time():", long_time())  # 0.08681082725524902 s
print("long_time2():", long_time2())  # 0.10457372665405273 s


print('----------------UNDER THE HOOD OF GENERATORS--------------------')


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)  # <list_iterator object at 0x7f01d33447c0> 4 times
            next(iterator)
        except StopIteration:
            break


special_for([1, 2, 3])


print('----------------CUSTOM RANGE GENERATORS--------------------')


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 10)

for i in gen:
    print(i)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


print('----------------EXERCISE: FIBONACCI NUMBERS--------------------')


def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        old_a = a
        a = b
        b = old_a + b


for item in fib(20):
    print("item:", item)


def fib2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        old_a = a
        a = b
        b = old_a + b
    return result


for item in fib2(20):
    print("item:", item)

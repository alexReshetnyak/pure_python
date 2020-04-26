print('---------------------------GENERATORS-----------------------')
# * Python generators are a simple way of creating iterators.
# * All the work we mentioned above are automatically handled by
# * generators in Python.
# * Simply speaking, a generator is a function that returns an
# * object (iterator) which we can iterate over (one value at a time).


default_list = list(range(10))
print("default_list:", default_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# or


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


print("make_list(10):", make_list(10))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


print('---------------------------GENERATORS2-----------------------')


def generator_function(num):
    for i in range(num):
        yield i * 2  # run next step


for item in generator_function(10):
    print("item:", item)  # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18

g = generator_function(10)
print("next(g):", next(g))  # 0
print("next(g):", next(g))  # 2

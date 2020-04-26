print('---------------------------FUNCTIONS 2--------------------------------')
print('---------------------------METHODS VS FUNCTIONS-----------------------')
# * Methods alway belong to objects (car.drive)

print('---------------------------DOC STRINGS--------------------------------')


def test(a):
    '''
    Info: This function tests and prints param a
    '''
    print("a:", a)  #


test('zzz')  # zzz
# help(test) # Info: This function tests and prints param a

# Info: This function tests and prints param a
print("test.__doc__:", test.__doc__)


print('---------------------------CLEAN CODE--------------------------------')


def is_even(num):
    return num % 2 == 0


print("is_even(50):", is_even(50))  # True


print('---------------------------*args and **kwargs (key word args)--------')
# * *args - make tuple from parameters
# * **kwargs - make dictionary from keyword arguments


def super_func(*args, **kwargs):
    print("args:", args)  # (1, 2, 3, 4, 5)
    print("kwargs:", kwargs)  # {'num1': 5, 'num2': 10}
    total = sum(args)
    for item in kwargs.values():
        total += item
    return total


print("super_func(1,2,3,4,5):", super_func(
    1, 2, 3, 4, 5, num1=5, num2=10))  # 30

# ---------------------------------------------------------------------------------
# * Rule oreder: params, *args, default_parametes, **kwargs


def super_func2(name, *args, i='hi', **kwargs):
    print("name:", name)  # 1
    print("i:", i)  # hi
    total = sum(args)
    for item in kwargs.values():
        total += item
    return total


print("super_func2(1,2,3,4,5):", super_func2(1, 2, 3, 4, 5, num1=5, num2=10))


print('---------------------------FUNCTION AS PARAMETER---------------------')


# * Pass function as parameter
def wrap(func, *args):
    return func(args[0])


wrap(test, 'Say hello!')  # Say hello!


print('---------------------------EXERCISE--------------------------------')


def highest_even(li):
    biggest_number = 0
    for number in li:
        if number > biggest_number and number % 2 == 0:
            biggest_number = number
    return biggest_number


def highest_even2(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print("highest_even2([10,2,3,4,8]):", highest_even2([10, 2, 3, 4, 8]))  # 10
print(":", )

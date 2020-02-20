print('---------------------------SCOPE--------------------------------')
# * Scope - what variables do I have access to?
total = 100  # * creates variable in global scope

# ------------------------------------------------------
# * Python has function scope (every new function creates it own scope)


def do_something():
    data = 'data'

# print("data:", data) # !  name 'data' is not defined


# ------------------------------------------------------
# * if, while, for and etc don't create new scope
if True:
    a = 'a'
print("a:", a)  # a


print('---------------------------SCOPE RULES--------------------------------')
# * 1 - start search with local scope
# * 2 - then look into Parent scope?
# * 3 - look in global
# * 4 - check if it built in function (like max, sum and etc)
a = 1


def confusion():
    a = 5   # * creates it one variable
    return a


print("confusion(), a:", confusion(), a)  # 5, 1

# -------------------------------------------------------
a = 1


def parent():
    a = 10

    def confusion():
        return a
    a = 11
    return confusion()


print("parent():", parent())  # 11


print('---------------------------GLOBAL KEYWORD--------------------------------')


def confusion2(b):
    # * Creates b in local scope
    print(b)


print("confusion():", confusion2(300))  # 300

# ---------------------------------------------
total = 0


def count():
    # * get total from global scope
    # ! bad practice to use global
    global total
    total += 1
    return total


print("count():", count())  # 1
print("count():", count())  # 2

# ------------------------------------------
# * DI
total = 0


def count2(total):
    total += 1
    return total


total = count2(total)
total = count2(total)
print("total:", total)  # 2


print('---------------------------NONLOCAL KEYWORD--------------------------------')


def outer():
    x = 'local'

    def inner():
        # * get variable from parent scope
        # ! doesn't work if parent scope is global
        nonlocal x
        x = 'nonlocal'
        print('inner x:', x)  # nonlocal

    inner()
    print('outher x:', x)  # nonlocal


outer()

print('---------------------------FUNCTIONS--------------------------------')
# ? we can run functions only after it was defined

# say_hello() # ! NameError: name 'say_hello' is not defined


def say_hello():
    phrase = 'Hello'
    print(":", phrase)


say_hello()  # Hello

# print(":", phrase) # ! NameError: name 'name' is not defined


print('---------------------------ARGUMENTS VS PARAMETERS--------------------')


def say_hello1(name):  # name - parameter
    phrase = 'Hello'
    print(":", f'{phrase} {name}')


say_hello1('Alexey')  # Hello Alexey , 'Alexey' is argument


print('---------------KEYWORD ARGUMENTS AND DEFAULT PARAMETERS---------------')


def say_hello2(name, second_name):
    phrase = 'Hello'
    print(":", f'{phrase} {name} {second_name}')


# ? Keyword arguments
# ! Bad practice
say_hello2(second_name='Reshetnyak', name='Alexey')  # Hello Alexey Reshetnyak

# --------------------------------------------------------------------------------
# ? Default parameters


def say_hello3(name='Darth', second_name='Vader'):
    phrase = 'Hello'
    print(":", f'{phrase} {name} {second_name}')


say_hello3()  # Hello Darth Vader
# say_hello2() # ! Error missing 2 required
# ! positional arguments: 'name' and 'second_name'


print('---------------------------RETURN--------------------------------')


def sum(num1, num2):
    num1 + num2


print("sum(1,4):", sum(1, 4))  # None

# ---------------------------------------------------


def sum1(num1, num2):
    return num1 + num2


total = sum1(2, 3)  # 5
print("sum1(1,total):", sum1(1, total))  # 6

# ---------------------------------------------------


def sum2(num1, num2):
    def another_func(num1, num2):
        return num1 + num2


total = sum2(1, 2)
print("sum2(1,2):", sum2(1, 2))  # None

# ----------------------------------------------------


def sum3(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func


total = sum3(1, 2)
# <function sum3.<locals>.another_func at 0x7fb8315ef950>
print("sum3(1,2):", sum3(1, 2))

# ----------------------------------------------------


def sum4(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


total = sum4(1, 2)
print("sum4(1,2):", sum4(1, 2))  # 3

print(":", )
print(":", )
print(":", )
print(":", )


print('---------------------------Error handling 2------------------------')


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers', err)


print("sum('1', 2):", sum('1', 2))  # 3


print('------------------Wrapping errors together----------------------------')


def sum2(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ValueError, ZeroDivisionError) as err:
        print('oops', err)


print("sum2('1')", sum2(1, 3))

print(":", )  #
print(":", )  #

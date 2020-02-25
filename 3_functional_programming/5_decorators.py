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
print("a:", a)  #  Still here!

print('---------------------------HIGHER ORDER FUNCTION--------------------------------')
# * HOC - The function that accept other function as parameter or return function as result


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


print(":", )  #
print(":", )  #
print(":", )  #
print(":", )  #

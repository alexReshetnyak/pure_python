print('---------------------------FUNCTIONS--------------------------------')
# ? we can run functions only after it was defined

# say_hello() # ! NameError: name 'say_hello' is not defined

def say_hello():
  phrase = 'Hello'
  print(":", phrase) #

say_hello() # Hello

# print(":", phrase) # ! NameError: name 'name' is not defined

print('---------------------------ARGUMENTS VS PARAMETERS--------------------------------')

def say_hello1(name): # name - parameter
  phrase = 'Hello'
  print(":", f'{phrase} {name}') #

say_hello1('Alexey') # Hello Alexey , 'Alexey' is argument

print(":", ) #
print(":", ) #

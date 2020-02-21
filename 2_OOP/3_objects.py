print('---------------------------SUPER--------------------------------')


class User():
    def __init__(self, email):
        self.email = email

        def sign_in(self):
            print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email) # * 1st way
        super().__init__(email)  # * 2 way
        self.name = name
        self.power = power


wizard = Wizard('Tom', 35, 'mail')

print("wizard.sign_in():", wizard.email)  # mail


print('---------------------------INTROSPECTION--------------------------------')
# * Ability to determine the type of an object at run time
# ['User', 'Wizard', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'wizard']
print(":", dir())

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'email', 'name', 'power']
print(":", dir(wizard))  # all methods and attributes that this object has access to
print(":", )  #
print(":", )  #

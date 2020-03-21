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


print('---------------------------INTROSPECTION---------------------------')
# * Ability to determine the type of an object at run time
# ['User', 'Wizard', '__annotations__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'wizard']
print(":", dir())

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', 'email', 'name', 'power']
# all methods and attributes that this object has access to
print(":", dir(wizard))


print('---------------------------DUNDER METHODS-----------------------------')


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Alex',
            'has_pets': False
        }

    def __str__(self):
        return self.color

    def __call__(self):
        return 'Yes how cool is that?'

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
# red
print("action_figure.__str__():", action_figure.__str__())
print("str(action_figure):", str(action_figure))  # red
print("action_figure():", action_figure())  # Yes how cool is that?
print("action_figure['name']:", action_figure['name'])  # Alex


print('---------------------------EXERCISE-----------------------------')


class SuperList(list):
    def __len__(self):
        return 9


new_list = SuperList()
new_list.append(5)

print("len(new_list):", len(new_list))  # 9
print("issubclass(SuperList, list):", issubclass(SuperList, list))  # True

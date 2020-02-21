print('---------------------------ENCAPSULATION--------------------------------')
# * Encapsulation refers to the bundling of data with the methods that operate on that data,
# * or the restricting of direct access to some of an object's components


print('---------------------------ABSTRACTION--------------------------------')
# * main goal is to handle complexity by hiding unnecessary details from the user.
# * That enables the user to implement more complex logic on top of the provided abstraction without
# * understanding or even thinking about all the hidden complexity.


class PlayerCharacter2:

    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    def speak(self):
        return f'Hi, I am {self.name}'


player2 = PlayerCharacter2('Tom', 20)
print("player2.speak():", player2.speak())  # Hi, I am Tom


print('---------------------------ABSTRACTION PRIVATE VS PUBLIC METHODS--------------------------------')


class PlayerCharacter3:
    # * __methodname__ - means Dunder method (build into Python)
    def __init__(self, name='anonymous'):
        self.name = name

    def speak(self):
        return f'Hi, I am {self.name}'

        # * private method by convention (but we steel can change it)
    def _speak(self):
        return f'Hi, I am {self.name}'


player3 = PlayerCharacter3('Tom')
player3.speak = "Can't speak"
print("player3.speak():", player3.speak)  # Can't speak


print('---------------------------INHERITANCE--------------------------------')
# * Inheritance allows us to define a class that inherits all the methods and properties from another class


class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attack with arrows {self.num_arrows}')


wizard = Wizard('Tom', 35)
archer = Archer('Robin', 200)

print("wizard.sign_in():", wizard.sign_in())  # logged in
print("wizard.attack():", wizard.attack())  # Attack with power of 35
print("archer.attack():", archer.attack())  # Attack with arrows 200


print('---------------------------INHERITANCE 2--------------------------------')

print("isinstance(archer, Archer):", isinstance(archer, Archer))  # True
print("isinstance(archer, User):", isinstance(archer, User))  # True
print("isinstance(archer, object):", isinstance(archer, object))  # True


print('---------------------------POLYMORPHISM--------------------------------')
# * Objects of different types can be accessed through the same interface.
# * Each type can provide its own, independent implementation of this interface.

print("wizard.attack():", wizard.attack())  # Attack with power of 35
print("archer.attack():", archer.attack())  # Attack with arrows 200

print(":", )
print(":", )

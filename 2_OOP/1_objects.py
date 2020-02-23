print('---------------------------OOP TYPES--------------------------------')


class BigObject:
    pass


obj1 = BigObject()

print("type(None):", type(None))            # <class 'NoneType'>
print("type(True):", type(True))            # <class 'bool'>
print("type(5):", type(5))                  # <class 'int'>
print("type(5.5):", type(5.5))              # <class 'float'>
print("type('Hi'):", type('Hi'))            # <class 'str'>
print("type([]):", type([]))                # <class 'list'>
print("type(()):", type(()))                # <class 'tuple'>
print("type({}):", type({}))                # <class 'dict'>
print("type(BigObject):", type(BigObject))  # <class 'type'>
print("type(obj1):", type(obj1))            # <class '__main__.BigObject'>


print('---------------------------CREATING OUR OWN OBJECTS-------------------')


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} run')
        return 'done'


player1 = PlayerCharacter('Alexey', 32)
player1.run()  # Alexey run
print("player1.age:", player1.age)  # 32


print('---------------------------ATTRIBUTES AND METHODS--------------------')
# help(player1)


class PlayerCharacter2:
    # * Class object attrebute
    membership = True

    def __init__(self, name='anonymous', age=0):
        # if PlayerCharacter2.membership:
        if self.membership:
            self.name = name
            self.age = age
            self.membership = False
            self.run()

    def run(self):
        print(f'{self.name} run')
        return 'done'


player2 = PlayerCharacter2('Alexey', 32)
print("player2.membership:", player2.membership)  # False
print("PlayerCharacter2.membership:", PlayerCharacter2.membership)  # True


print('---------------------------@classmethod @staticmethod-----------------')


class PlayerCharacter3:

    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def create_teddy(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things_static(num1, num2):
        return num1 + num2


player3 = PlayerCharacter3('Tom', 20)

print("player3.adding_things(1,2):", player3.adding_things(1, 2))  # 3
print(
    "PlayerCharacter3.adding_things(1,2):",
    PlayerCharacter3.adding_things(1, 2)
)  # 3

teddy = PlayerCharacter3.create_teddy(5, 2)
print("teddy:", teddy)  # <__main__.PlayerCharacter3 object at 0x7f9bbd915fd0>
print(
    "teddy.adding_things_static(1,2):",
    teddy.adding_things_static(1, 2)
)  # 3
print(
    "PlayerCharacter3.adding_things_static(1,2):",
    PlayerCharacter3.adding_things_static(1, 2)
)  # 3

print(":", )  #


print('---------------------------OBJECTS 2--------------------------------')


class PlayerCharacter:

    def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

    def run(self):
        return self


player = PlayerCharacter('Tom', 20)
# <__main__.PlayerCharacter object at 0x7feb8a21cd90>
print("player.run():", player.run())
# <__main__.PlayerCharacter object at 0x7feb8a21cd90>
print("player.run().run():", player.run().run())

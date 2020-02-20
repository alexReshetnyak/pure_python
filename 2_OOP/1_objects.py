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


print('---------------------------CREATING OUR OWN OBJECTS--------------------------------')


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} run')
        return 'done'


player1 = PlayerCharacter('Alexey', 32)
player1.run()  # Alexey run
print("player1.age:", player1.age) # 32


print(":", )

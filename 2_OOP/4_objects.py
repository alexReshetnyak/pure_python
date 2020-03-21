print('---------------------------MULTIPLE INHERITACE------------------------')


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with power of {self.power}')

    def run(self):
        print('Run really fast')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attack with arrows {self.num_arrows}')

    def check_arrows(self):
        print(f'You have {self.num_arrows} arrows')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('name', 30, 50)
print("hb1.attack():", hb1.attack())  # Attack with power of 30
print("hb1.run():", hb1.run())  # Run really fast

# ! AttributeError: 'HybridBorg' object has no attribute 'num_arrows'
# ! Will be error without custom __init__ method
print("hb1.check_arrows():", hb1.check_arrows())  # You have 50 arrows


print('---------------------------MRO METHOD RESOLUTION ORDER----------------')
# * Depth First Search
# *    A
# *   / \
# *  /   \
# * B     C
# *  \   /
# *   \ /
# *    D


class A():
    num = 1


class B(A):
    pass


class C(A):
    num = 10


class D(B, C):
    pass


print("D.num:", D.num)  # 10
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>]
print("D.mro():", D.mro())  #


# --------------------------------------------------------
class X:
    pass


class Y:
    pass


class Z:
    pass


class A1(X, Y):
    pass


class B1(Y, Z):
    pass


class M(B1, A1, Z):
    pass


# * (<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>,
# * <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>,
# * <class 'object'>)
print("M.__mro__:", M.__mro__)

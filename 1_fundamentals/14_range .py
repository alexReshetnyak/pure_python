print('---------------------------RANGE--------------------------------')
# ? Object that produce a sequence of integers from start to stop

print("range(100):", range(100))  # range(0, 100)

for number in range(0, 5):
    print("number:", number)  # 0,1,2,3,4,5

print(":", )  #

for _ in range(0, 5):
    print(":", 'send email')  # use _ if you don't need variable

print(":", )  #

for number in range(0, 10, 2):
    print("number:", number)  # 0,2,4,6,8

print(":", )  #

for number in range(10, 0, -2):  # back count
    print("number:", number)  # 10, 8, 6, 4, 2

print(":", )  #

print('---------------------------LIST COMPREHENSIONS--------------------------------')

my_list = [char for char in 'iterable']
print("my_list:", my_list)  # ['i', 't', 'e', 'r', 'a', 'b', 'l', 'e']

my_list2 = [num for num in range(0,10)]
print("my_list2:", my_list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list3 = [num*2 for num in range(0,10)]
print("my_list3:", my_list3)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

my_list4 = [num**2 for num in range(0,10) if num % 2 == 0]
print("my_list4:", my_list4)  # [0, 4, 16, 36, 64]

print(":", )  #
print(":", )  #
print(":", )  #
print(":", )  #

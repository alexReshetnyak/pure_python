print('---------------------------LIST COMPREHENSIONS--------------------------------')

my_list = [char for char in 'iterable']
print("my_list:", my_list)  # ['i', 't', 'e', 'r', 'a', 'b', 'l', 'e']

my_list2 = [num for num in range(0, 10)]
print("my_list2:", my_list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list3 = [num*2 for num in range(0, 10)]
print("my_list3:", my_list3)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

my_list4 = [num**2 for num in range(0, 10) if num % 2 == 0]
print("my_list4:", my_list4)  # [0, 4, 16, 36, 64]


print('---------------------------SET COMPREHENSIONS--------------------------------')
my_set5 = {char for char in 'iterable'}
print("my_set5:", my_set5)  # {'l', 'a', 'r', 'b', 'i', 't', 'e'}

my_set6 = {num for num in range(0, 10)}
print("my_set6:", my_set6)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set7 = {num*2 for num in range(0, 10)}
print("my_set7:", my_set7)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

my_set8 = {num**2 for num in range(0, 10) if num % 2 == 0}
print("my_set8:", my_set8)  # {0, 4, 16, 36, 64}


print('---------------------------DICTIONARY COMPREHENSIONS--------------------------------')
simple_dict = {
  'a': 1,
  'b': 2
}

my_dict = { k:v**2 for k,v in simple_dict.items() if v%2 == 0 }
print("my_dict:", my_dict)  # {'b': 4}

my_dict2 = { i:i*2 for i in [1,2,3] }
print("my_dict2:", my_dict2)  # {1: 2, 2: 4, 3: 6}


print('---------------------------EXERCISE COMPREHENSIONS--------------------------------')
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({char for char in some_list if some_list.count(char) > 1})

print("duplicates:", duplicates) #  ['n', 'b']


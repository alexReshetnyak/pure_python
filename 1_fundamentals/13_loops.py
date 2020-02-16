print('---------------------------LOOPS--------------------------------')
for item in [1,2,3]:
  print("item number:", item) # 1, 2, 3

print("item:", item) # 3
print(":", ) #

for item in 'string':
  print("item string:", item) # s, t, r, i, n, g

print(":", ) #

for item in {'a': 1, 'b': 2}:
  print("item dictionary:", item) # a, b


print('---------------------------ITERABLES--------------------------------')
# ? iterable - list, dictionary, set, tuple, string
for item in {'a': 1, 'b': 2}.items():
  print("item, tuples from dictionary:", item) # ('a', 1), ('b', 2)

print(":", ) #

for item in {'a': 1, 'b': 2}.values():
  print("item, values from dictionary:", item) # 1, 2

print(":", ) #
  
for item in {'a': 1, 'b': 2}.keys():
  print("item, keys from dictionary:", item) # a, b

print(":", ) #

for key, value in {'a': 1, 'b': 2}.items():
  print("key, value:", key, value) # a 1, b 2


print('---------------------------EXERCISE COUNTER--------------------------------')
my_list = [1,2,3,4,5,6,7,8,9,10]

total = 0
for value in my_list:
  total += value

print("total:", total) # 55

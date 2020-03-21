print('---------------------------DICTIONARY--------------------------------')
# dict
dictionary = {
    'a': [1, 2, 3],
    'b': 2,
    'x': True,
}

print('dictionary["b"]:', dictionary['b'])  # 2
# ! print("dictionary['b']:", dictionary['c']) #  Error


print('---------------------------DICTIONARY KEYS---------------------------')
# ? For keys we can use strings, booleans, numbers, tuples
# ? (only immutable types) and should be uniq
dictionary = {
    123: [1, 2, 3],
    # [2]: 2,
    2.2: 2,
    True: 'boolean',  # will be removed
    True: True,
    (1, 2, 3): [1, 2, 3],
}

print("dictionary[123]:", dictionary[123])  # [1,2,3]
print("dictionary[True]:", dictionary[True])  # True
print("dictionary[2.2]:", dictionary[2.2])  # 2
# print("dictionary[[2]]:", dictionary[[2]]) # ! Error unhashable type: 'list'


print('---------------------------DICTIONARY METHODS-------------------------')
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
}

print("user.get('age'):", user.get('age'))  # None
print("user.get('age'):", user.get('age', 55))  # 55
print("user.get('basket'):", user.get('basket'))  # [1, 2, 3]

user2 = dict(name='John')
print("user2:", user2)  # {'name': 'John'}

print('------------------DICTIONARY METHODS 2----------------------------')

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
}

print("'basket' in user:", 'basket' in user)  # True
print("'basket' in user:", 'hello' in user)  # False
print("'basket' in user.keys():", 'basket' in user.keys())  # True
print("'hello' in user.values():", 'hello' in user.values())  # True
# dict_items([('basket', [1, 2, 3]), ('greet', 'hello')])
print("user.items():", user.items())

user2 = user.copy()
print("user.clear():", user.clear())  # None
print("user:", user)  # {}
print("user2:", user2)  # {'basket': [1, 2, 3], 'greet': 'hello'}

# [1, 2, 3] , remove item and return value
print("user2.pop('basket'):", user2.pop('basket'))
# print("user2.pop('basket'):", user2.pop('basket')) # ! Error
# ('greet', 'hello') , remove SOME item and return key value as a tuple
print("user2.popitem():", user2.popitem())
# print("user2.popitem():", user2.popitem()) # # ! Error  dictionary is empty'
user['age'] = 55
# None, update or create certain value
print("user.update({'age': 18}):", user.update({'age': 18}))
# None, update or create certain value
print("user.update({'age': 18}):", user.update({'ages': 44}))
user['age'] = 20
print("user:", user)  # {'age': 20, 'ages': 44}
print(":", )

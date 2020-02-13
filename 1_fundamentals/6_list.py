print('---------------------------LIST (Array)--------------------------------')
li = [1,2,3,4,5]
print('li:', li) # [1, 2, 3, 4, 5]
print('li[3]:', li[3]) # 4
#print('li[5]:', li[5]) # ! Error list index out of range


print('---------------------------LIST SLICING--------------------------------')
# List is mutable
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]

amazon_cart[0] = 'Laptop'
print('amazon_cart[0:2]:', amazon_cart[0:2]) # ['Laptop', 'sunglasses']
print('amazon_cart[0::2]:', amazon_cart[0::2]) # ['Laptop', 'toys']
new_list = amazon_cart[1:3]
print('new_list:', new_list) # ['sunglasses', 'toys'] get slice of old array

amazon_cart2 = amazon_cart
amazon_cart3 = amazon_cart[:]
amazon_cart2[0] = 'gum'
print('amazon_cart2[0]:', amazon_cart2[0]) # gum
print('amazon_cart[0]:', amazon_cart[0]) # gum amazon_cart == amazon_cart2
print('amazon_cart3[0]:', amazon_cart3[0]) # Laptop amazon_cart != amazon_cart3


print('---------------------------MATRIX--------------------------------')
matrix = [
  [1,2,3],
  [2,4,6],
  [7,8,9]
]

print('matrix[0][1]', matrix[0][1]) # 2


print('---------------------------LIST METHODS--------------------------------')
basket = [1,2,3,4,5]
print('len(basket):', len(basket)) # 5

print('basket.append(6):', basket.append(6)) # None, like push adds value to the end
print('basket:', basket) # [1, 2, 3, 4, 5, 6]

print('basket.insert(0):', basket.insert(0, 0)) # None, (position, value)  adds value to the position
print('basket:', basket) # [0, 1, 2, 3, 4, 5, 6]

print('basket.extend([7,8]):', basket.extend([7,8])) # None, merge to array (like js concat)
print('basket:', basket) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

print('basket.pop():', basket.pop()) # 8, delete from the end (like js pop)
print('basket:', basket) # [0, 1, 2, 3, 4, 5, 6, 7]

print('basket.pop(1):', basket.pop(1)) # 1, remove with index
print('basket:', basket) # [0, 2, 3, 4, 5, 6, 7]

print('basket.remove(0):', basket.remove(0)) # None, find and remove value
print('basket:', basket) # [2, 3, 4, 5, 6, 7]

print('basket.clear():', basket.clear()) # None, remove all items from list
print('basket:', basket) # []


print('---------------------------LIST METHODS 2--------------------------------')
basket = ['a','b','c','d','e','e']

print('basket.index("b"):', basket.index('b')) # 1, find index of value

# print('basket.index("d", 0, 2):', basket.index('d', 0, 2)) # Error, start index, end index where to search
print('basket.index("d", 0, 8):', basket.index('d', 0, 8)) # 3, start index, end index where to search

print('"d" in basket:', "d" in basket) # True
print('"x" in basket:', "x" in basket) # False

print('"i" in basket:', "i" in 'hi my name is') # True

print('basket.count("e"):', basket.count("e")) # 2 Count value


print('---------------------------LIST METHODS 3--------------------------------')
basket = ['a','b','e','c','d','e']
basket2 = basket.copy()

print('basket.sort():', basket.sort()) # None, sort list
print('basket:', basket) #  ['a', 'b', 'c', 'd', 'e', 'e']

print('sorted(basket2):', sorted(basket2)) # ['a', 'b', 'c', 'd', 'e', 'e']

print('basket.reverse():', basket.reverse()) # None
print('basket:', basket) #  ['e', 'e', 'd', 'c', 'b', 'a']


print('---------------------------LIST PATTERNS--------------------------------')

print('basket[::-1]:', basket[::-1]) # ['a', 'b', 'c', 'd', 'e', 'e'], Reverse again and return copy
print('basket:', basket) #  ['e', 'e', 'd', 'c', 'b', 'a']

print('range(1,100)', range(1,100)) # range(1, 100), creates range
print('list(range(1,100))', list(range(1,100))) # [1, 2 ... 98, 99] creates list with values from 1 to 99
print('list(range(100))', list(range(100))) # [0, 1 ... 98, 99] creates list with values from 0 to 99

sentence = 'Default'
new_sentence = sentence.join(['Hi','my','name','is','Alexey'])
print('sentence:', sentence) # Default
print('new_sentence:', new_sentence) # HiDefaultmyDefaultnameDefaultisDefaultAlexey

new_sentence2 = ' '.join(['Hi','my','name','is','Alexey'])
print('new_sentence2:', new_sentence2) # Hi my name is Alexey


print('---------------------------LIST UNPACKING--------------------------------')
basket = [1,2,3,4,5,6,7,8,9]
a, b, c, *other, d = basket # *variable_name works like js rest (...rest)

print('a:', a) # 1
print('b:', b) # 2
print('c:', c) # 3
print('other:', other) # [4, 5, 6, 7, 8]
print('d:', d) # 9
print('basket:', basket) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

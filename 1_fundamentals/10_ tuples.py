print('---------------------------TUPLES--------------------------------')
# like list but we can't modify it (immutable)

my_tuple = (1,2,3,4,5)
#my_tuple[1] = 'z' # ! TypeError: 'tuple' object does not support item assignment

print("my_tuple[0]:", my_tuple[0]) # 1
print("2 in my_tuple:", 2 in my_tuple) # True

dictionary = {
  123: [1,2,3],
  (1,2,3): [1,2,3], # * tuple as a key
}

print("dictionary[(1,2,3)]:", dictionary[(1,2,3)]) # [1, 2, 3]

print('---------------------------TUPLES 2--------------------------------')

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]

print("new_tuple:", new_tuple) # (2,)

x, y, z, *other = my_tuple
print("x:", x) # 1
print("y:", y) # 2
print("z:", z) # 3
print("other:", other) # [4, 5], returns list

my_tuple = (1,2,3,4,5)
print("my_tuple.count():", my_tuple.count(5)) # 1, count matches
print("my_tuple.index(2):", my_tuple.index(2)) # 1, indexOf 2
print("len(my_tuple):", len(my_tuple)) # 5
print(":", ) #

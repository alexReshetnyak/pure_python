print('---------------------------TUPLES--------------------------------')
# like list but we can't modify them (immutable)

my_tuple = (1,2,3,4,5)
#my_tuple[1] = 'z' # ! TypeError: 'tuple' object does not support item assignment

print("my_tuple[0]:", my_tuple[0]) # 1
print("2 in my_tuple:", 2 in my_tuple) # True

dictionary = {
  123: [1,2,3],
  (1,2,3): [1,2,3], # * tuple as a key
}

print("dictionary[(1,2,3)]:", dictionary[(1,2,3)]) # [1, 2, 3]
print(":", ) #

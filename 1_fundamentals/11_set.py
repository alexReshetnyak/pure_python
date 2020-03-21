print('---------------------------SET--------------------------------')
# ? Unordered collection of uniq objects
my_set = {1, 2, 3, 4, 5}
print("my_set:", my_set)  # {1, 2, 3, 4, 5}
my_set = {1, 2, 3, 4, 5, 5}
print("my_set:", my_set)  # {1, 2, 3, 4, 5} , only uniq values

my_set.add(100)  # return None
my_set.add(2)
print("my_set:", my_set)  # {1, 2, 3, 4, 5, 100}


my_list = [1, 2, 3, 4, 5, 5]
my_uniq_list = list(set(my_list))
print("my_uniq_list:", my_uniq_list)  # [1, 2, 3, 4, 5]

my_set = {1, 2, 3, 4, 5}
# print("my_set[0]:", my_set[0]) # ! Error 'set' object is not subscriptable
print("1 in my_set:", 1 in my_set)  # True
print("len(my_set):", len(my_set))  # 5
print("list(my_set):", list(my_set))  # [1, 2, 3, 4, 5]

new_set = my_set.copy()
print("new_set:", new_set)  # {1, 2, 3, 4, 5}


print('---------------------------SET 2--------------------------------')
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9}

print("my_set.difference(your_set):", my_set.difference(your_set))  # {1, 2, 3}
print(":", my_set.discard(5), my_set)  # None, {1, 2, 3, 4}, remove 5 from set
# None,  remove all duplicate elements
print(":", my_set.difference_update(your_set), )
print("my_set:", my_set)  # {1, 2, 3}

my_set = {1, 2, 3, 4, 5}
print("my_set.intersection(your_set):", my_set.intersection(
    your_set))  # {4, 5} return duplicates
print("my_set:", my_set)  # {1, 2, 3, 4, 5}
print("{1,2} & {2,3}:", {1, 2} & {2, 3})  # {2} other way to return duplicates

print(":", my_set.isdisjoint(your_set))  # False, sets have duplicates

# {1, 2, 3, 4, 5, 6, 7, 8, 9}, merge
print("my_set.union(your_set):", my_set.union(your_set))
# {1, 2, 3, 4}, other way to merge sets
print("{1,2} | {3,4}:", {1, 2} | {3, 4})

print(
    "{1,2}.issubset({1,2,3,4}):",
    {1, 2}.issubset({1, 2, 3, 4})
)  # True, Check if this set the part of another set

print(
    "{1,2,3,4}.issuperset({1,2}):",
    {1, 2, 3, 4}.issuperset({1, 2})
)  # True, Check if this set has all values from another set

print(":", )
print(":", )

from functools import reduce

print('---------------------------MAP--------------------------------')
# * creates new map object that we can change to list


def multiply_by2(item):
    return item * 2


result = map(multiply_by2, [1, 2, 3])
print("result:", result)  # <map object at 0x7f1a16e525d0>
print("list(result):", list(result))  # [2, 4, 6]


print('---------------------------FILTER--------------------------------')
# * should return boolean
my_list = [1, 2, 3, 4]


def only_odd(item):
    return item % 2 != 0


# <filter object at 0x7f8472540f50>
print("filter(only_odd, my_list):", filter(only_odd, my_list))
print(
    "list(filter(only_odd, my_list)):",
    list(filter(only_odd, my_list))
)  # [1, 3]


print('---------------------------ZIP--------------------------------')
my_list = [1, 2, 3, 4]
your_list = [10, 20, 30]
your_list2 = (10, 20, 30)

print(
    "list(zip(my_list, your_list)):",
    list(zip(my_list, your_list))
)  # [(1, 10), (2, 20), (3, 30)]
print(
    "list(zip(my_list, your_list2)):",
    list(zip(my_list, your_list2))
)  # [(1, 10), (2, 20), (3, 30)]


print('---------------------------REDUCE--------------------------------')
my_list = [1, 2, 3, 4]


def accumulator(acc, item):
    return acc + item


print(
    "reduce(accumulator, my_list, 0):",
    reduce(accumulator, my_list, 0)
)  # 10

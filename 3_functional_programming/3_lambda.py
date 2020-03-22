from functools import reduce

print('---------------------------LAMBDA EXPRESSIONS-------------------------')
# * anonymous function that you use once
# * and has implicit return

result = map(lambda item: item * 2, [1, 2, 3])
result2 = filter(lambda item: item % 2 != 0, [1, 2, 3])
result3 = reduce(lambda acc, item: acc + item, [1, 2, 3])
print("result:", list(result))  # [2, 4, 6]
print("list(result2):", list(result2))  # [1, 3]
print("result3:", result3)  # 6


print('---------------------------LAMBDA EXERCISE----------------------------')

my_list = [5, 4, 3]

print(
    "list(map(lambda number: number*number,my_list)):",
    list(map(lambda number: number**2, my_list))
)  # [25, 16, 9]


# --------------------------------------------------------
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(
    "ist(sorted(a, key=lambda item: item[1])):",
    list(sorted(a, key=lambda item: item[1]))
)  # [(10, -1), (0, 2), (4, 3), (9, 9)]
print("a:", a)  # [(0, 2), (4, 3), (9, 9), (10, -1)]
print(
    "a.sort(key=lambda x: x[1])",
    a.sort(key=lambda x: x[1])
)  # None
print("a:", a)  # [(10, -1), (0, 2), (4, 3), (9, 9)]

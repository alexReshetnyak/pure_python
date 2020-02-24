print('---------------------------PURE FUNCTIONS--------------------------------')
# * 1 same input always gives same output
# * 2 no side effects, they should only return result


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print("multiply_by2([2,3,4,5]):", multiply_by2([2, 3, 4, 5]))  # [4, 6, 8, 10]

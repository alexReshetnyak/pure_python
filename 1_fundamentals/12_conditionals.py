print('---------------------------CONDITIONALS-----------------------------')
is_old = False
is_licenced = True

if is_old and is_licenced:
    print("'You are old!':", 'You are old!')  # 'You are old!'
elif is_licenced or is_old:
    # 'You licenced already'
    print("'You licenced already':", 'You licenced already')
else:
    print("'You are yong':", 'You are yong')  # 'You are yong'


print('---------------------------TRUTHY FALSEY------------------------------')

print("bool(''):", bool(''))  # False
print("bool(None):", bool(None))  # False
print("bool(0):", bool(0))  # False
print("bool([]):", bool([]))  # False
print("bool({}):", bool({}))  # False
print("bool(()):", bool(()))  # False
print("bool(1):", bool(1))  # True
print("bool('string'):", bool('string'))  # True
print("bool({'asd': 'test'}):", bool({'asd': 'test'}))  # True
print("bool({'asd','test'}):", bool({'asd', 'test'}))  # True
print("bool(('asd','test')):", bool(('asd', 'test')))  # True


print('---------------------------TERNARY OPERATOR--------------------------------')
is_friend = True

# It is a friend
print("'It is a friend':", 'It is a friend') if is_friend else print("'No':", 'No')


print('---------------------------SHORT CIRCUITING--------------------------------')

is_friend = True
is_user = True
name = False or 'Alex'
name2 = 'Alex' and False
print("is_friend and is_user:", is_friend and is_user)  # True
print("is_friend or is_user:", is_friend or is_user)  # True
print("name:", name)  # Alex
print("name2:", name2)  # False


print('---------------------------LOGICAL OPERATORS----------------------')
# ? >
# ? <
# ? ==
print("4 > 5:", 4 > 5)  # False
print("4 <= 5:", 4 <= 5)  # True
print("4 == '4':", 4 == '4')  # False
# ! TypeError: '>' not supported between instances of 'int' and 'str'
# print("4 > '4':", 4 > '4') 
print("4 >= '4':", 4 >= int('4'))  # True
print("'a' > 'b':", 'a' > 'b')  # False
print("'a' < 'b':", 'a' < 'b')  # True
print("'a' > 'A':", 'a' > 'A')  # True
print("4 != '4':", 4 != '4')  # True


print("not(True):", not(True))  # False
print("not True:", not True)  # False


print('---------------------------EXERCISE--------------------------------')
is_magician = True
is_expert = False

if is_magician and is_expert:
    print(":", 'You are master magician')
elif is_magician and not is_expert:
    # 'At least you are getting there'
    print(":", 'At least you are getting there')
elif not is_magician:
    print(":", 'You need magic power')


print('---------------------------is vs ==--------------------------------')
# ? == check for equality (with type converting)
# ? is  check  (without type converting)

print("True == 1:", True == 1)            # True
print("True is 1:", True is 1)            # False

print("'' == 1:", '' == 1)                # False
print("'' is 1:", '' is 1)                # False

print("'1' == 1:", '1' == 1)              # False
print("'1' is 1:", '1' is 1)              # False

print("10 == 10.0:", 10 == 10.0)          # True
print("10 is 10.0:", 10 is 10.0)          # False

print("[] == 1:", [] == 1)                # False
print("[] is 1:", [] is 1)                # False

print("[] == 0:", [] == 0)                # False
print("[] is 0:", [] is 0)                # False

print("[1] == 1:", [1] == 1)              # False
print("[1] is 1:", [1] is 1)              # False

print("[] == []:", [] == [])              # True
print("[] is []:", [] is [])              # False

print("[1,2] == [1,3]:", [1, 2] == [1, 3])  # False
print("[1,2] is [1,3]:", [1, 2] is [1, 3])  # False

print("[1,2] == [1,2]:", [1, 2] == [1, 2])  # True
print("[1,2] is [1,2]:", [1, 2] is [1, 2])  # False


print(":", )

print('---------------------------VARIABLES--------------------------------')
# ! snake_case
# ! start with lowercase or underscore
# ! letters, numbers, underscores
# ! case sensitive
# ! don't overwrite keywords
# ! _user - private variable


user_iq = 190
user_age = user_iq/4
print('iq', user_iq) # 190
print('user_age', user_age) # 47.5

print('---------------------------CONSTANTS--------------------------------')
PI = 3.14 # You can change it but you shouldn't
PI = 4
print('PI', PI) # 190

print('---------------------------MULTIPLE ASSIGNMENTS--------------------------------')
a,b,c = 1,2,3
print('a', a) # 1
print('b', b) # 2
print('c', c) # 3

print('---------------------------EXPRESSIONS VS STATEMENTS--------------------------------')
iq = 150
user_age = iq / 5 # * (user_age = iq / 5) - statement, (iq / 5) - expression
print('user_age', user_age) # 30.0

print('---------------------------AUGMENTED ASSIGNMENT OPERATOR--------------------------------')
some_value = 5
# some_value = some_value + 5
some_value += 5 # AUGMENTED assignment operato
print('some_value', some_value) # 10

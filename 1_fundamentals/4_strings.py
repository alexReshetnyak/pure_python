print('---------------------------STRINGS--------------------------------')
some_str = "text"
print('type(some_str):', type(some_str))  # str

user_name = 'supercoder'
password = 'pass'

long_string = '''
WOW
0 0
---
'''
print('long_string:', long_string)


print('---------------------------STRINGS CONCATENATIONS--------------------')
first_name = 'Alexey'
last_name = 'Reshetnyak'
full_name = first_name + ' ' + last_name
# full_name  = first_name + 5 # ! Error
full_name = full_name + ' ' + str(5)
print('full_name:', full_name)  # Alexey Reshetnyak 5

print('---------------------------ESCAPE SEQUENCES--------------------------')
weather = "\t It\'s \"kind of\" sunny \\"  # * \t - tab, \n - new line
print('weather:', weather)  # It's "kind of" sunny \


print('---------------------------FORMATED STRING----------------------------')
name = 'Alexey'
age = 32

print('name:', 'Hi ' + name + '. You are ' + str(age) +
      ' years old')  # Hi Alexey. You are 32 years old
print('name:', 'Hi {}. You are {} years old'.format(
    name, str(age)))  # Hi Alexey. You are 32 years old
# Hi Alexey. You are 32 years old
print('name:', f'Hi {name}. You are {str(age)} years old')

print('---------------------------STRING INDEXES----------------------------')
# * name[start:finish:stepover]
print('name[0]:', name[0])  # A
print('name[1:3]:', name[1:3])  # le
print('name[1:5:2]):', name[1:5:2])  # lx
print('name[1:]:', name[1:])  # lexey
print('name[:5]:', name[:5])  # Alexe
print('name[::2]:', name[::2])  # Aee
print('name[-2]:', name[-2])  # e
print('name[::-1]:', name[::-1])  # yexelA (reverse string)

print('---------------------------IMMUTABILITY-------------------------------')
# ! Strings are immutable we can change them
name2 = 'Roma'
# ! name2[0] = 'D' # Error


print('---------------------------BUILTIN FUNCTIONS AND METHODS--------------')
print('len(name):', len(name))  # 6
print('name[:]:', name[:])  # Alexey
print('name[:len(name)]:', name[:len(name)])  # Alexey

quote = 'to be or not to be'
print('quote.upper():', quote.upper())  # TO BE OR NOT TO BE
print('quote.capitalize():', quote.capitalize())  # To be or not to be
print("quote.find('be'):", quote.find('be'))  # 3
# to me or not to me (return new string)
print("quote.replace('be', 'me'):", quote.replace('be', 'me'))
print('quote:', quote)  # to be or not to be

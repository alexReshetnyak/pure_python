print('---------------------------STRINGS--------------------------------')
some_str = "text"
print('type(some_str):', type(some_str)) # str

user_name = 'supercoder'
password = 'pass'

long_string = '''
WOW
0 0
---
'''
print('long_string:',long_string)



print('---------------------------STRINGS CONCATENATIONS--------------------------------')
first_name  = 'Alexey'
last_name   = 'Reshetnyak'
full_name   = first_name + ' ' + last_name
#full_name  = first_name + 5 # ! Error
full_name  = full_name + ' ' + str(5)
print('full_name:', full_name) # Alexey Reshetnyak 5

print('---------------------------ESCAPE SEQUENCES--------------------------------')
weather = "\t It\'s \"kind of\" sunny \\" # * \t - tab, \n - new line
print('weather:', weather) # It's "kind of" sunny \


print('---------------------------FORMATED STRING--------------------------------')
name = 'Alexey'
age = 32

print('name:', 'Hi ' + name + '. You are ' + str(age) + ' years old') # Hi Alexey. You are 32 years old
print('name:', 'Hi {}. You are {} years old'.format(name, str(age))) # Hi Alexey. You are 32 years old
print('name:', f'Hi {name}. You are {str(age)} years old') # Hi Alexey. You are 32 years old

print('---------------------------STRING INDEXES--------------------------------')
print('name[0]:', name[0]) # A
print('name[1:3]:', name[1:3]) # le
print('name[1:5:2]):', name[1:5:2]) # lx
print('name[1:]:', name[1:]) # lexey
print('name[:5]:', name[:5]) # Alexe
print('name[::2]:', name[::2]) # Aee
print('name[-2]:', name[-2]) # e
print('name[::-1]:', name[::-1]) # yexelA (reverse string)

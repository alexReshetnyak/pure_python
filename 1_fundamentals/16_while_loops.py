print('---------------------------WHILE LOOPS--------------------------------')

i = 1
while i < 5:
    print(":", i)  # 1, 2, 3, 4
    i += 1

print(":", )

i = 1
while i < 5:
    print(":", i)  # 1
    break

print(":", )

i = 1
while i < 3:
    print(":", i)  # 1,2
    i += 1
else:
    print("'The work is done':", 'The work is done')  # The work is done


print(":", )

i = 1
while i < 3:
    print(":", i)  # 1,2
    break
else:
    # This part will not run (break)
    print("'The work is done':", 'The work is done')


print('---------------------------WHILE LOOPS 2------------------------------')

i = 1
while True:
    try:
        # answer = input('Guess my age ')
        answer = '32'
        if int(answer) is 32:
            print(":", 'You are right!')
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


print('---------------------------BREAK CONTINUE PASS------------------------')
# ? for while and for loops
# ? break - stop whole loop
# ? continue - go to the next iteration step
# ? pass - do nothing

print('---------------------------EXERCISE GUI-------------------------------')

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

fill = '*'
empty = ' '

for row in picture:
    string = ''
    for pixel in row:
        string += fill if pixel else empty
    print(":", string)


print('---------------------------EXERCISE FIND DUPLICATES-------------------')
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for char in some_list:
    if some_list.count(char) > 1 and char not in duplicates:
        duplicates.append(char)
print("duplicates:", duplicates)  # ['b', 'n']

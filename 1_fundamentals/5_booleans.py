print('---------------------------BOOLEANS--------------------------------')
# bool (True, False)
name = 'Alexey'
is_cool = False
is_cool = True
print('bool(1):', bool(1)) # ? True
print('bool(0):', bool(0)) # ? False
print('bool("string"):', bool('string')) # ? True
print('bool(""):', bool('')) # ? False

print('---------------------------EXERCISE TYPE CONVENTION--------------------------------')
from datetime import date
name = 'Alexey'
relationship_status = 'single'
relationship_status = '\"married\"'

born_year = input('What year were you born? ')
current_year = int(date.today().year)
age = current_year - int(born_year)

print("f'Your age is 33'", f'Your age is: {age}') # 33
print("2019 - bool(2019)", 2019 - bool(2019)) # 2018 (Boolens become 1 or 0)

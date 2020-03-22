print('---------------------------Error handling------------------------')

while True:
    try:
        age = int(input('What is your age? '))
        print("age:", age)  #
        10/age
        # * throw own error
        # raise ValueError('Hey cut it out')
    # * catch only value errors (Exception = all exceptions)
    except (ValueError, Exception):
        print(":", f'Invalid age!')  #
    except ZeroDivisionError:  # catch only value errors
        print(":", f'Please enter number higher than zero!')  #
    else:
        print('Thank you!')
        break
    finally:
        print('Done!')

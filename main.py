
import string
import random

# Define all mixed capitalization, upper caps, lower caps, digits, and special chars in variables.
mixed = string.ascii_letters
upper = string.ascii_uppercase
lower = string.ascii_lowercase
dig = string.digits
special = string.punctuation

# # String randomizer function
# def generate_pass(my_str):
#     string_list = list(my_str)
#     random.shuffle(string_list)
#     random_string = ''.join(string_list)
#     return random_string


pass_length = int(input('Enter length of desired password: '))
user_pass = ''

if pass_length >= 4:
    # Variable to hold if digits are included
    digits = input('Include digits? Y/N: ').upper()
    # Variable to hold if special characters are included
    special_char = input('Include special chars? Y/N: ').upper()
    mixed_cases = input('Mixed upper and lower case? Y/N: ').upper()
    if mixed_cases == 'N':
        upper_or_lower_case = input('Upper case only? Y/N: ').upper()
        if upper_or_lower_case == 'Y':
            user_pass += upper
        elif upper_or_lower_case == 'N':
            user_pass += lower
        else:
            print('Invalid input!')
    if mixed_cases == 'Y':
        user_pass += mixed
    else:
        print('Invalid Input!')
    # Conditionals for including digits or not
    if digits == 'Y':
        user_pass += dig
    elif digits == 'N':
        pass
    else:
        print('Invalid input!')
    # Conditionals for including special chars or not
    if special_char == 'Y':  
        user_pass += special
    
else:
    print('Password length should be greater than 4!')
print(user_pass)

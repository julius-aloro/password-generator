
import string
import random

# Define all mixed capitalization, upper caps, lower caps, digits, and special chars in variables.
mixed = string.ascii_letters
upper = string.ascii_uppercase
lower = string.ascii_lowercase
dig = string.digits
special = string.punctuation

# String randomizer function
def randomizer(string):
    string_list = list(string)
    random.shuffle(string_list)
    random_string = ''.join(string_list)
    return random_string


pass_length = int(input('Enter length of desired password: '))
passwd = ''

if pass_length >= 4:
    mix_cases = input('Mixed upper and lower case? Y/N: ')
    if mix_cases == 'Y':
        randomizer(mixed)
else:
    print('Password length should be greater than 4.')
        



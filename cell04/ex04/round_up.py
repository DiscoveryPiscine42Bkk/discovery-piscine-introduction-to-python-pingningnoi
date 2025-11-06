import math
import sys

user_input = input("Give me a number: ")

try:
    number_float = float(user_input)

    rounded_number = int(math.ceil(number_float))

    print(rounded_number)
        
except ValueError:
    sys.exit(1)
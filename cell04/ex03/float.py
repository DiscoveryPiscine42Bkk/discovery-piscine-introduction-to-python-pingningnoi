user_input = input("Give me a number: ")

try:
    number_float = float(user_input)
 
    if number_float == int(number_float):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
        
except ValueError:
    print("Invalid input: Please enter a number.")
    exit(1)

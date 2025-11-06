import sys

def downcase_it(input_string):
    return input_string.lower()

parameters = sys.argv[1:]
num_parameters = len(parameters)

if num_parameters == 0:
    print("none")

else:
    for param in parameters:
        result = downcase_it(param)
        print(result)
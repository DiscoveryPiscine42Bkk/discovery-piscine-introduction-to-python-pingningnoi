import sys

parameters = sys.argv[1:]
num_parameters = len(parameters)

if num_parameters < 2:
    print("none")

else:
    reversed_parameters = parameters[::-1]
    
    for param in reversed_parameters:
        print(param)
import sys

parameters = sys.argv[1:]
num_parameters = len(parameters)

if num_parameters < 2:
    print("none")
else:
    for param in parameters[::-1]:
        print(param)
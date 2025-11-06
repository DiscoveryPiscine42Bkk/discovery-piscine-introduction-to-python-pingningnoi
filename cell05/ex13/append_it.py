import sys

parameters = sys.argv[1:]
num_parameters = len(parameters)

if num_parameters == 0:
    print("none")

else:
    for param in parameters:
        if not param.endswith("ism"):
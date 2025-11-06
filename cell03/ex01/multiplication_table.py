try:
    number = int(input("Enter a number\n")) 
except ValueError:
    exit(1)

for i in range(10): 
    result = i * number

    print(f"{i} x {number} = {result}")
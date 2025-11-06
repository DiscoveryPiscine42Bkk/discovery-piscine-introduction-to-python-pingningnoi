try:
    num1 = float(input("Give me the first number: "))
except ValueError:
    print("Invalid input for the first number.")
    exit(1)

try:
    num2 = float(input("Give me the second number: "))
except ValueError:
    print("Invalid input for the second number.")
    exit(1)

print("Thank you!")

print(f"{num1} + {num2} = {num1 + num2}")

print(f"{num1} - {num2} = {num1 - num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print(f"{num1} / {num2} = Cannot divide by zero")

print(f"{num1} * {num2} = {num1 * num2}")
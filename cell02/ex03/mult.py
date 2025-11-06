number1 = int(input("Enter the first number:\n")) 

number2 = int(input("Enter the second number:\n")) 

result = number1 * number2

print(f"{number1} x {number2} = {result}")

if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
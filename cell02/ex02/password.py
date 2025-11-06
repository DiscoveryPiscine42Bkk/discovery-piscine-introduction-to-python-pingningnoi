CORRECT_PASSWORD = "Python is awesome"

user_input = input("Enter password: ").strip() 

if user_input == CORRECT_PASSWORD:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED.")
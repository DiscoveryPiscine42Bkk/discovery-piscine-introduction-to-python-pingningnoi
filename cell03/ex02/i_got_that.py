first_run = True

while True:
    
    if first_run:
        user_input = input("What you gotta say?\n").strip() 
        first_run = False 
    else:
        user_input = input("I got that! Anything else?:\n").strip()

    if user_input == "STOP":
        break  
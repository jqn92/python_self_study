def int_test():
    while True:
        try:
            user_input = int(input("Write a number: "))
            print(f"Your number is: {user_input}")
            break
        except ValueError:
            print("Try again.")

int_test()
    
                 

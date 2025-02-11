def factors(n):
    m = 1
    if n <= 0:
        print("Please, enter a positive number.")
    else:
        for m in range(1, n+1):
            if n % m == 0:
                print(f"{m} is a factor of {n}.")
        

# factor: (m <= n) and ((n % m) == 0)

user_number = int(input("Enter a positive integer: "))
factors(user_number)

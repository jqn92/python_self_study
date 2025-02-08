# Write a function that doubles a number input. Then loops the function 3 times and displays the result.

def doubles(num):
    """Take a number and double it."""
    result = num * 2
    return result

test_number = int(input("Enter your number: "))

for x in range(3):
    test_number = doubles(test_number)
    print(test_number)

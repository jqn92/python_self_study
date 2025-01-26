# Displays if the difference between 2 numbers is an integer
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
result = (num1-num2).is_integer()
print(f"The difference between {num1} and {num2} is an integer? {result}!")

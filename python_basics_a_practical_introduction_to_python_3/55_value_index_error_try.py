str1 = input("Write something: ")

while True:
    try:
        n = int(input("Write a number: "))
        print(f"The character at index {n} is {str1[n]}.")
        break
    except ValueError:
        print(f"You should write a number. Try again.")
    except IndexError:
        print(f"'{str1}' is less than {n} characters long. Try again.")

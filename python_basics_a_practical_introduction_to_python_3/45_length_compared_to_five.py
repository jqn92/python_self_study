# Prompts the user to enter a word and analyzes whether it is less than, greater than or equal to 5 characters long.

user_word = input("Enter a word:")

def length_compared_to_five(word):
    """Compare the length of a string and display whether it's less than, greater than or equal to 5 characters long."""
    if len(word) < 5:
        print(f"The word '{word}' is less than 5 characters long.")
    elif len(word) > 5:
        print(f"The word '{word}' is more than 5 characters long.")
    else:
        print(f"The word '{word}' is exactly 5 characters long.")

length_compared_to_five(user_word)

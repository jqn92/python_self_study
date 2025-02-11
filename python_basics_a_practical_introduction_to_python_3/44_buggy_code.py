# Debugged code final version

def add_underscores(word):
    new_word = "_"
    for char in word:
        new_word = new_word + char + "_"
    return new_word

phrase = "hello"
print(add_underscores(phrase))

# Debugged code version 1
#
# def add_underscores(word):
#     new_word = "_"
#     for i in range(0, len(word)):
#         new_word = new_word + word[i] + "_"
#     return new_word
#
# phrase = "hello"
# print(add_underscores(phrase))

# print() method for debugging
#
# def add_underscores(word):
#     new_word = "_"
#     for i in range(0, len(word)):
#         new_word = word[i] + "_"
#         print(f"i = {i}; new_word = {new_word}")
#     return new_word
#
# phrase = "hello"
# print(add_underscores(phrase))


# Original, buggy code
#
# def add_underscores(word):
#    new_word = "_"
#    for i in range(0, len(word)):
#        new_word = word[i] + "_"
#    return new_word
#
# phrase = "hello"
# print(add_underscores(phrase))

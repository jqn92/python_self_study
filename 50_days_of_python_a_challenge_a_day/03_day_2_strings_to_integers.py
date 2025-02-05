# Page 11

# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

def convert_add(strings_list):
    for string in range(len(strings_list)):
        strings_list[string] = int(strings_list[string])
    print(sum(strings_list))

convert_add(["1","3","5"])
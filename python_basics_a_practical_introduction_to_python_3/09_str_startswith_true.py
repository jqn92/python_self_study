# Corrects 08_str_startswith.py so that the method returns True to all of them
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "   bEautiful"
print(string1.lower().startswith("be"))
print(string2.startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lower().lstrip().startswith("be"))

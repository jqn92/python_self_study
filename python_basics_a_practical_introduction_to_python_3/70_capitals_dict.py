capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"
    }

key_value_pairs = (("California", "Sacramento"),("New York", "Albany"), ("Texas", "Austin"))

capitals_from_tuple = dict(key_value_pairs)

# print(capitals)
# print(capitals_from_tuple)

print(capitals["Texas"])

capitals["Colorado"] = "Denver"

print(capitals)

for state, capital in capitals.items():
    print(f"The capital of {state} is {capital}.")

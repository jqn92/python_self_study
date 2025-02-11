captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"

if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

del captains["Discovery"]

print(captains)

key_values = (('Enterprise', 'Picard'), ('Voyager', 'Janeway'), ('Defiant', 'Sisko'))

captains_dict = dict(key_values)

print(captains_dict)

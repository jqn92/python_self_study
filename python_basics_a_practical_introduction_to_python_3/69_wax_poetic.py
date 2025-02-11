# Solved with Real Python's repository help

import random

noun = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verb = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjective = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
preposition = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverb = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def make_poem():
    noun1 = random.choice(noun)
    noun2 = random.choice(noun)
    noun3 = random.choice(noun)

    while noun1 == noun2:
        noun2 = random.choice(noun)
    while noun1 == noun3 or noun2 == noun3:
        noun3 = random.choice(noun)

    verb1 = random.choice(verb)
    verb2 = random.choice(verb)
    verb3 = random.choice(verb)

    while verb1 == verb2:
        verb2 = random.choice(verb)
    while verb1 == verb3 or verb2 == verb3:
        verb3 = random.choice(verb)

    adjective1 = random.choice(adjective)
    adjective2 = random.choice(adjective)
    adjective3 = random.choice(adjective)

    while adjective1 == adjective2:
        adjective2 = random.choice(adjective)
    while adjective1 == adjective3 or adjective2 == adjective3:
        adjective3 = random.choice(adjective)

    preposition1 = random.choice(preposition)
    preposition2 = random.choice(preposition)
    preposition3 = random.choice(preposition)

    while adjective1 == adjective2:
        preposition2 = random.choice(preposition)
    while preposition1 == preposition3 or preposition2 == preposition3:
        preposition3 = random.choice(preposition)

    adverb1 = random.choice(adverb)
    adverb2 = random.choice(adverb)
    adverb3 = random.choice(adverb)

    while adverb1 == adverb2:
        adverb2 = random.choice(adverb)
    while adverb1 == adverb3 or adverb2 == adverb3:
        adverb3 = random.choice(adverb)
    
    poem = (
        f"A/An {adjective1} {noun1}\n\n"
        f"A/An {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}\n"
        f"{adverb1}, the {noun1} {verb2}\n"
        f"the {noun2} {verb3} {preposition2} a {adjective3} {noun3}"
    )

    return poem

poem = make_poem()
print(poem)

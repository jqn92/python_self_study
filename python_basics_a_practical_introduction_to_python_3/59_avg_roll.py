import random

def die_roll():
    """Simulate rolls and return the average number rolled in x attempts."""
    roll = 0
    total = 0
    number_of_rolls = int(input("Enter how many times you want to roll the die: "))
    for trial in range(number_of_rolls):
        roll = random.randint(1,6)
        # print(roll) for testing with small rolls
        total = total + roll
        
    return print(f"After rolling {number_of_rolls} times, the average number rolled is {round(total/number_of_rolls)}.")

die_roll()

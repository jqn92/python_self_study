import random

heads = 0
tails = 0

while True:
    try:
        flips = int(input("Enter how many times you want to flip the coin: "))
        for flip in range(flips):
            if random.randint(0,1) == 0:
                heads = heads + 1
            else:
                tails = tails + 1
        break
    except ValueError:
        print("Please, enter a number for your flips: ")
        
print(f"You got {heads} heads in {flips} flips.")
print(f"You got {tails} tails in {flips} flips.")
print(f"The ratio of heads to tails is {heads/tails}.")

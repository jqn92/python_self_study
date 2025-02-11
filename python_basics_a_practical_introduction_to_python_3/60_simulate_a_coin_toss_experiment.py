import random

def coin_flip():
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"


# Real Python's repository solution

flips = 0

num_trials = 10

for trial in range(num_trials):
    if coin_flip() == "heads":
        flips = flips + 1
        while coin_flip() == "heads":
            flips = flips + 1
        flips = flips + 1
    else:
        flips = flips + 1
        while coin_flip() == "tails":
            flips = flips + 1
        flips = flips + 1

avg_flips_per_trial = flips/num_trials
print(f"The average number of flips per trial for the sequence to contain both heads and tails is {avg_flips_per_trial}.")

# My (wrong) attempt
#
# flips = []
#
# i=0
#
# for i in range(10):
#     print(flips)
#     if flips[i] != flips[i-1]:
#         break
#     else:
#         continue
#     if coin_flip() == "heads":
#         flips.append("heads")  
#     else:
#         flips.append("tails")
#        
# print(f"The average number of flips per trial for the sequence to contain both heads and tails is {(len(flips)+1)/i}.")

import random

regions_won_by_a = 0
regions_won_by_b = 0

elections_won_by_a = 0
elections_won_by_b = 0

num_trials = 10_000

for trial in range(num_trials):
    if random.randint(0,1) <= .87:
        regions_won_by_a = regions_won_by_a + 1
    else:
        regions_won_by_b = regions_won_by_b + 1
        
    if random.randint(0,1) <= .65:
        regions_won_by_a = regions_won_by_a + 1
    else:
        regions_won_by_b = regions_won_by_b + 1
        
    if random.randint(0,1) <= .17:
        regions_won_by_a = regions_won_by_a + 1
    else:
        regions_won_by_b = regions_won_by_b + 1
        
    if regions_won_by_a > regions_won_by_b:
        elections_won_by_a = elections_won_by_a + 1
    else:
        elections_won_by_b = elections_won_by_b + 1

percentage_a = round((elections_won_by_a/num_trials)*100)
percentage_b = round((elections_won_by_b/num_trials)*100)

print(f"Candidate A won the {percentage_a}% of {num_trials} simulated elections.")
print(f"Candidate B won the {percentage_b}% of {num_trials} simulated elections.")

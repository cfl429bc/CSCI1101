# standard dev of random numbs
import random
import sys

count = int(input("How many random numbers? "))
if count < 1:
    print("Need at least one number!")
    sys.exit()

lower = float(input("Lower bound? "))
upper = float(input("Upper bound? "))

if lower > upper:
    print("The lower bound cannot be more than the upper bound")
    sys.exit()
elif lower == upper:
    print("The lower bound cannot equal the upper bound")
    sys.exit()

vals = []
while len(vals) < count:
    vals.append(random.uniform(lower,upper))

sum = 0
for val in vals:
    sum += val

mean = sum / count

diffs = 0
for val in vals:
    diffs += ((val - mean) ** 2)

avg_diffs = diffs / count

std_dev = (avg_diffs ** 0.5)

print(f"Mean = {mean:.3f}")
print(f"Standard Deviation = {std_dev:.3f}")
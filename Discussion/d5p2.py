# standard dev of random numbs
import random
count = 15
vals = []
while len(vals) < count:
    vals.append(random.uniform(0,100))

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
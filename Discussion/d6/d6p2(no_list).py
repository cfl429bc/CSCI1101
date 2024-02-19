import sys

len = int(input("How many numbers do you have? "))
if len <= 0:
    sys.exit()

print(f"Enter the {len} numbers each on their own line:")
      
i = 0
pos = 0
zero = 0
neg = 0

while i < len:
    val = float(input())
    
    if val > 0:
        pos += 1
    elif val == 0:
        zero += 1
    elif val < 0:
        neg += 1
    i += 1

p_pos = (pos / len) * 100
p_zero = (zero / len) * 100
p_neg = (neg / len) * 100

print(f"{p_pos:.2f}% positive values.")
print(f"{p_zero:.2f}% zero values.")
print(f"{p_neg:.2f}% negative values.")
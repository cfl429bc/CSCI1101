import math
import sys

func = str(input("Enter log, ln, or log2: "))
val = float(input("Enter a value: "))
if func == "log":
    out = math.log10(val)
elif func == "ln":
    out = math.log(val)
elif func == "log2":
    out = math.log2(val)
else:
    print("That's not a valid operation!")
    sys.exit()

print(f"{func}({val:.3f}) = {out:.3f}")
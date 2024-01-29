import math
function = str(input("Enter log, ln, or log2: "))
value = float(input("Enter a value: "))
if function == "log":
    output = math.log10(value)
    print(f"log({value:.3f}) = {output:.3f}")
elif function == "ln":
    output = math.log(value)
    print(f"ln({value:.3f}) = {output:.3f}")
elif function == "log2":
    output = math.log2(value)
    print(f"log2({value:.3f}) = {output:.3f}")
else:
    print("That's not a valid operation!")
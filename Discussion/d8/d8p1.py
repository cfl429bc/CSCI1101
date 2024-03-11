import sys

def reverse(string):
    new_string = ""
    i = len(string)-1
    while i >= 0:
        new_string += string[i]
        i -= 1
    return new_string


print("Enter some text, quit to stop:")
for line in sys.stdin:
    line = line.strip()
    if line.lower() == "quit":
        sys.exit()
    print(reverse(line))
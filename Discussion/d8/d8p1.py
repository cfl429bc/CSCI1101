import sys

def reverse(string):
    chars = []
    for char in string.strip():
        chars.append(char)
    print(chars)
    while i > 0:
        new_string.append(string[i])
        i -=1
    return new_string

def is_palindromes(string):

    return True

# Enter some text, quit to stop: 
# Week 8
# 8 keeW
# Python functions are super fun.
# .nuf repus era snoitcnuf nohtyP
# quit

lines = []
text = []

print("Enter some text, quit to stop:")
for line in sys.stdin:
    if line.strip().lower() == "quit":
        sys.exit()
    chars = []
    for char in line.strip():
        chars.append(char)
    print(line.strip())
    print(chars)
    rev = reverse(chars)
    print(rev)
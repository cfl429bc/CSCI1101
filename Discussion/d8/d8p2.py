import sys

def reverse(string):
    new_string = ""
    i = len(string)-1
    while i >= 0:
        new_string += string[i]
        i -= 1
    return new_string

def is_palindrome(string):
    string = remove_punctuation(string)
    if string.lower() == reverse(string.lower()):
        return True
    else:
        return False

def remove_punctuation(string):
    string = list(string)
    new_string = []
    for char in string:
        if char.isalnum():  
            new_string.append(char)
    return "".join(new_string)

print("Enter some text, quit to stop:")
for line in sys.stdin:
    line = line.strip()
    if line.lower() == "quit":
        sys.exit()
    if is_palindrome(line):
        print("That's a palindrome!")
    else:
        print("Nope.")
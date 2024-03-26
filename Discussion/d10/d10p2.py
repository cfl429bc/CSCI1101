import sys

def analyze_file(file):
    lines = 0
    words = 0
    chars = 0
    for line in file:
        lines += 1
        word_list = line.strip().split()
        words += len(word_list)
        chars += len(line)
    return lines,words,chars

my_list = []
# filename = input("Enter the input file name: ")
fileinput = input("Enter the input file name: Discussion/d10/")
filename = "Discussion/d10/" + fileinput


try:
    with open(filename) as input_file:
        lines,words,chars = analyze_file(input_file)
        print(f"# Lines: {lines}")
        print(f"# Words: {words}")
        print(f"# Chars: {chars}")
        
    
except OSError:
    print(f"Error with {filename}!")
    sys.exit()

import sys

my_list = []
filename = "Qzzz_files/q4p7input.txt"
try:
    with open(filename) as input_fh:
        for line in input_fh:
            values = line.split()
            my_list.append(values)
except OSError:
    print(f"Error opening {filename}!")
    sys.exit()

print(my_list[2])
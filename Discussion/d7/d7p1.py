import sys

def posinput(string):
    num = int(input(f"Enter a value for {string}: "))
    if num <= 0:
        print(f"{string} must be positive!")
        sys.exit()
    return num

num_1 = posinput("A")
num_2 = posinput("B")

# did not finish this
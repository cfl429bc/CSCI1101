import sys

def split_file(input_file,int_out,float_out,string_out):
    for line in input_file:
        words = line.split()
        for word in words:
            if is_int(word) == True:
                print(word, file=int_out)
            elif is_float(word) == True:
                print(word, file=float_out)
            else:
                print(word, file=string_out)
    
def is_int(datam):
    try:
        int(datam)
        return True
    except ValueError:
        return False

def is_float(datam):
    try:
        float(datam)
        return True
    except ValueError:
        return False

def get_name(file_type):
    return input(f"Enter the {file_type} file name: ")

# input_name = get_name("input")
input_name = "mixed.txt"
# int_out_name = get_name("integer output")
int_out_name = "ints.txt"
# float_out_name = get_name("float output")
float_out_name = "floats.txt"
# string_out_name = get_name("string output")
string_out_name = "strs.txt"

try:
    with (
    open(input_name) as input_file,
    open(int_out_name, "w") as int_out,
    open(float_out_name, "w") as float_out,
    open(string_out_name, "w") as string_out
    ):
        split_file(input_file,int_out,float_out,string_out)
        print(int_out.tell())
        int_out.truncate(int_out.tell()-1)
        float_out.truncate(float_out.tell()-1)
        string_out.truncate(string_out.tell()-1)
        
except OSError:
    print(f"File Error!")
    sys.exit()
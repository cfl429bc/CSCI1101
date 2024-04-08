import sys

def is_float(datam):
    try:
        float(datam)
        return True
    except ValueError:
        return False
    
def get_name(file_type):
    return input(f"Enter the {file_type} file name: ")
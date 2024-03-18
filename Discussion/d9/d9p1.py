import sys

def check_sorted(list):
    for i in range(len(list)-1):
            if list[i] > list[i+1]:
                return False
    return True

test1 = [1,2,3,4,5,6,6,7]
test2 = [2,5,2,5,7]
test3 = []
print(f"test1 = {check_sorted(test1)}")
print(f"test2 = {check_sorted(test2)}")
print(f"test3 = {check_sorted(test3)}")
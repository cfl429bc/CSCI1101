def binary_search(nums, target):
    if len(nums) == 0:
        return False
    
    mid = int(len(nums)/2)
    if nums[mid] == target:
        return True
    
    if target > nums[mid]:
        return binary_search(nums[mid+1:], target)
    else:
        return binary_search(nums[:mid], target)


my_list = [4, 10, 11, 24, 26,
27, 32, 33, 61, 63,
64, 72, 74, 75, 79,
86, 92, 93, 98, 100]
seek = int(input("Enter the value to search for: "))
if binary_search(my_list, seek):
    print(f"{seek} was in the list!")
else:
    print(f"{seek} was not in the list!")

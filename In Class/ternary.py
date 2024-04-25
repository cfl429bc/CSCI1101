def ternary_search(nums, target):
    if len(nums) == 0:
        return False
    
    left = int(len(nums)/3)
    right = int((len(nums)*2)/3)
    if nums[left] == target or nums[right] == target:
        return True
    
    if target < nums[left]:
        return ternary_search(nums[:left], target)
    elif target > nums[right]:
        return ternary_search(nums[right+1:], target)
    else:
        return ternary_search(nums[right+1:left], target)


my_list = [4, 10, 11, 24, 26,
27, 32, 33, 61, 63,
64, 72, 74, 75, 79,
86, 92, 93, 98, 100]
seek = int(input("Enter the value to search for: "))
if ternary_search(my_list, seek):
    print(f"{seek} was in the list!")
else:
    print(f"{seek} was not in the list!")

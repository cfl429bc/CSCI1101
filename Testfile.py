def reverse_order(some_list):
    rev_list = []
    for i in range(len(some_list)-1, -1, -1):
        rev_list.append(some_list[i])
        print(i)
    return rev_list
values = [1, 2, 3, 4]
result = reverse_order(values)
# this will print [4, 3, 2, 1]
print(result)

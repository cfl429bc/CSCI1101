def reverse_order(some_list):
    rev_list = [some_list[i] for i in range(len(some_list)-1, -1, -1)]
    return rev_list
values = [1, 2, 3, 4]
result = reverse_order(values)
# this will print [4, 3, 2, 1]
print(result)

# a = [[1,2,3], [4,5,6]]
# transpose = []
# for j in range(len(a[0])):
#     transpose.append([])
#     for i in range(len(a)):
#         transpose[j].append(a[i][j])
# print(transpose)

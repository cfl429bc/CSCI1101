# def get_int(prompt):
#     value = int(input(prompt))
#     return value

# def factorial(n):
#     total = 1
#     while n > 0:
#         total *= n
#         n -= 1
#     return total

# def factor_sum(n):
#     total = 0
#     while n > 0:
#         total += n
#         n -= 1
#     return total

# def test_function(input_1, input_2):
#     print(f"Input 1 = {input_1}, and Input 2 = {input_2}")


# test = factorial(int(input("factorial of: ")))
# print(f"factorial = {test}")

# test = factor_sum(int(input("factor sum of: ")))
# print(f"factor sum = {test}")


# C = 299792458  
# def mass_to_energy(mass):
#     energy = mass * (C ** 2)
#     return energy

# def energy_to_mass(energy):
#     mass = energy / (C ** 2)
#     return mass

# energy = mass_to_energy(float(input("Mass to convert: ")))
# print(f"Energy = {energy}")

# mass = energy_to_mass(float(input("Energy to convert: ")))
# print(f"Mass = {mass}")



# def posinput(string):
#     num = int(input(f"Enter a value for {string}: "))
#     if num <= 0:
#         print(f"{string} must be positive!")
#         sys.exit()
#     return num

# def factortest(num, n): # outputs the factors, or 0 if not a factor
#     zero = 0
#     remain = num % n
#     if remain == 0:
#         return n
#     else:
#         return zero # if this is not included it outputs the string "none"

# def f(a, b):
#     result = ""
#     for c in a:
#         if c.isalpha():
#             result += c
#     for c in b:
#         if not c.isalpha():
#             result += c
#     print(result)

# s = "x=42,right?"
# f(s, s)

# -----------------------------------------------------------------------------------------------

# def merge_lists(list1,list2):
#     merged = []
#     len_min = min(len(list1),len(list2))
#     for i in range(max(len(list1),len(list2))):
#         if i <= (len_min - 1):
#             merged.append(list1[i] + list2[i])
#         else:
#             if len(list1) > len_min:
#                 merged.append(list1[i])
#             if len(list2) > len_min:
#                 merged.append(list2[i])
#     return merged

# def check_sorted(list):
#     for i in range(len(list)-1):
#             if list[i] > list[i+1]:
#                 return False
#     return True


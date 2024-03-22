def f(some_dictionary):
    some_dictionary["nagata"] = 2
    some_dictionary = {}
    return some_dictionary

ids = {"holden": 1, "draper": 4}
f(ids)
print(len(ids))
import sys

def key_of_longest_value(dict):
    if len(dict) == 0:
        return
    key_val = ""
    for key in dict:
        if key_val == "" or len(dict[key]) > len(dict[key_val]):
            key_val = key
    return key_val


maps = {"a": "apple",
        "b": "bookie",
        "c": "tacocat"}
key = key_of_longest_value(maps)
print(key)

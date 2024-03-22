stuff = {"5": "3",
         "a": "6",
         "q": "b",
         "3": "#",
         "+": "a"}

o="36b+5q"
n=""
for c in o:
    if c not in stuff:
        continue
    n += stuff[c]
print(n)
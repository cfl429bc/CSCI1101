import sys

def merge_lists(list1,list2):
    merged = []
    len_min = min(len(list1),len(list2))
    for i in range(max(len(list1),len(list2))):
        if i <= (len_min - 1):
            merged.append(list1[i] + list2[i])
        else:
            if len(list1) > len_min:
                merged.append(list1[i])
            if len(list2) > len_min:
                merged.append(list2[i])
    return merged

firsts = ["Peggy", "Natasha", "Bruce", "Thor"]
lasts = ["Carter", "Romanoff", "Banner"]
fulls = merge_lists(firsts, lasts)
print(fulls)
rev_fulls = merge_lists(lasts, firsts)
print(rev_fulls)
# fulls will be ["PeggyCarter", "NatashaRomanoff", "BruceBanner"]

a = float(input("Side A Length: "))
b = float(input("Side B Length: "))
c = float(input("Side C Length: "))

if a == b == c:
    print("Equalateral Triangle")
elif a != b and a != c and b != c:
    print("Scalene Triangle")
else:
    print("Isosolece Triangle")
    
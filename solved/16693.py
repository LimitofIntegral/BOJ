from math import pi
a, p1 = map(int, input().split())
r, p2 = map(int, input().split())

if a / p1 < (r * r * pi) / p2:
    print("Whole pizza")
else:
    print("Slice of pizza") 
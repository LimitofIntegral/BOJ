n = int(input())
t = n % 3

if (n / 3) % 2:
    print("CY" if t == 1 else "SK")
else:
    print("SK" if t == 1 else "CY")

# ??
a1 = [0, 1, 2, 3, 4, 5, 7, 8]
a2 = [6, 9]

arr = list(map(int, input()))
c = {}

for i in arr:
    try: c[i] += 1
    except: c[i] = 1


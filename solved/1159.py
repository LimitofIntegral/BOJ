n = int(input())

name = {}

for _ in range(n):
    t = input()[0]
    try: name[t] += 1
    except: name[t] = 1

name = sorted(name.items())

result = ""

for i in name:
    if i[1] >= 5:
        result += i[0]

if len(result):
    print(result)
else:
    print("PREDAJA")
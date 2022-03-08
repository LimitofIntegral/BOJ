a, b = map(list, input().split())

min_a, min_b, max_a, max_b = "", "", "", ""

for i in a:
    if i == '5' or i == '6':
        min_a += '5'
        max_a += '6'
    else:
        min_a += i
        max_a += i

for i in b:
    if i == '5' or i == '6':
        min_b += '5'
        max_b += '6'
    else:
        min_b += i
        max_b += i

print(int(min_a) + int(min_b), int(max_a) + int(max_b))
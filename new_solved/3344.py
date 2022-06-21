n = int(input())
odd = [i for i in range(1, n + 1) if i % 2]
even = [i for i in range(1, n + 1) if not i % 2]

if n % 2 and n % 3:
    for i in odd:
        print(i)
    for i in even:
        print(i)
else:
    if not n % 2:
        odd[0], odd[1] = odd[1], odd[0]
        odd = odd[0:2] + odd[3:] + [5]
    
    if not n % 3:
        even = even[1:] + even[:1]
        odd = odd[2:] + odd[:2]
    
    for i in even:
        print(i)
    for i in odd:
        print(i)
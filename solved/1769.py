t = ["3", "6", "9"]
number = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}

n = list(input())
count = 0

while len(n) > 1:
    count += 1
    c = {}
    for i in n:
        try: c[i] += 1
        except: c[i] = 1
    
    result = 0
    for i in c:
        result += number[i] * c[i]
    
    n = list(str(result))
    

print(count)
print("YES" if n[0] in t else "NO")
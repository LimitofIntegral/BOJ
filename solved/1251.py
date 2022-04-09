s = input()
l = len(s)
arr = []

for i in range(l - 2):
    for j in range(i + 1, l - 1):
        a, b, c = s[0:i + 1], s[i + 1:j + 1], s[j + 1:]
        arr.append(a[::-1] + b[::-1] + c[::-1])
        
arr.sort()
print(arr[0])
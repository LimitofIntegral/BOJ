arr = []
c = []

while True:
    temp = input()
    if temp == "E-N-D":
        break
    arr += input().split()

print(arr)
print(len(arr))

# 정규표현식 나중에 보고 다시 도전할 것
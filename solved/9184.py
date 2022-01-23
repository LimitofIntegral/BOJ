from itertools import product

dict = {}

dict[(0, 0, 0)] = 1

def call(i):
    if i[0] <= 0 or i[1] <= 0 or i[2] <= 0:
        return 1

    if i[0] > 20 or i[1] > 20 or i[2] > 20:
        t = (20, 20, 20)
        if t in dict:
            return dict[t]
        else:
            call(t)

    if i[0] < i[1] and i[1] < i[2]:
        r = 0
        t1 = (i[0], i[1], i[2] - 1)
        t2 = (i[0], i[1] - 1, i[2] - 1)
        t3 = (i[0], i[1] - 1, i[2])
        if t1 in dict:
            r += dict[t1]
        else:
            r += call(t1)
        if t2 in dict:
            r += dict[t2]
        else:
            r += call(t2)
        if t3 in dict:
            r -= dict[t3]
        else:
            r -= call(t3)
        return r
    
    r = 0
    t1 = (i[0] - 1, i[1], i[2])
    t2 = (i[0] - 1, i[1] - 1, i[2])
    t3 = (i[0] - 1, i[1], i[2] - 1)
    t4 = (i[0] - 1, i[1] - 1, i[2] - 1)
    if t1 in dict:
        r += dict[t1]
    else:
        r += call(t1)
    if t2 in dict:
        r += dict[t2]
    else:
        r += call(t2)
    if t3 in dict:
        r += dict[t3]
    else:
        r += call(t3)
    if t4 in dict:
        r -= dict[t4]
    else:
        r -= call(t4)
    return r

arr = [i for i in range(1, 21)]

for i in product(arr, repeat = 3):
    if i in dict:
        pass
    else:
        dict[i] = call(i)

temp = tuple(map(int, input().split()))

while True:
    print("w" + str(temp) + " =", call(temp))

    temp = tuple(map(int, input().split()))
    if temp == (-1, -1, -1):
        break
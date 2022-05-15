n = int(input())
arr = list(map(int, input().split()))
result = 0

for k in range(n):
    p = arr[k]
    left = [arr[i] for i in range(0, k + 1) if arr[i] <= p]
    right = [arr[i] for i in range(n - 1, k, -1) if arr[i] < p]
    temp = 0

    if left:
        result_l = [left[0]]
        for i in range(len(left)):
            if left[i] > result_l[-1]:
                result_l.append(left[i])
            else:
                lb = 0
                while left[i] > result_l[lb]:
                    lb += 1
                result_l[lb] = left[i]
        temp += len(result_l)
    if right:
        result_r = [right[0]]
        for i in range(len(right)):
            if right[i] > result_r[-1]:
                result_r.append(right[i])
            else:
                lb = 0
                while right[i] > result_r[lb]:
                    lb += 1
                result_r[lb] = right[i]
        temp += len(result_r)
    
    result = max(result, temp)

print(result)

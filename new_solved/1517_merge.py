import sys
input = sys.stdin.readline

def merge(l, r):
    global cnt
    if l < r:
        m = (l + r) // 2
        merge(l, m)
        merge(m + 1, r)

        a, b = l, m + 1
        temp = []
        while a <= m and b <= r:
            if arr[a] <= arr[b]:
                temp.append(arr[a])
                a += 1
            else:
                temp.append(arr[b])
                b += 1
                cnt += (m - a + 1)
        
        if a <= m:
            temp += arr[a:m + 1]
        if b <= r:
            temp += arr[b:r + 1]
        
        for i in range(len(temp)):
            arr[l + i] = temp[i]


n = int(input())
arr = list(map(int, input().split()))
cnt = 0
merge(0, n - 1)
print(cnt)
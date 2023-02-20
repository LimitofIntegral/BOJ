import sys
input = sys.stdin.readline

def hist(row):
    stack = []
    top, max_area, area, i = 0, 0, 0, 0

    while i < c:
        if not stack or row[stack[-1]] <= row[i]:
            stack.append(i)
            i += 1
        else:
            top = row[stack[-1]]
            stack.pop()
            if stack:
                area = top * (i - stack[-1] - 1)
                m[top] = max(m[top], (i - stack[-1] - 1))
            else:
                area = top * i
                m[top] = max(m[top], i)
            max_area = max(area, max_area)
    
    while stack:
        top = row[stack[-1]]
        stack.pop()

        if stack:
            area = top * (i - stack[-1] - 1)
            m[top] = max(m[top], (i - stack[-1] - 1))
        else:
            area = top * i
            m[top] = max(m[top], i)
        max_area = max(area, max_area)
    
    return max_area


def Rect():
    result = hist(arr[0])

    for i in range(1, r):
        for j in range(c):
            if arr[i][j]:
                arr[i][j] += arr[i - 1][j]
        result = max(result, hist(arr[i]))
    
    return result


r, c = map(int, input().split())

while r and c:
    m = [0] * 1001
    arr = [list(map(int, input().split())) for _ in range(r)]
    print(Rect())
    
    r, c = map(int, input().split())
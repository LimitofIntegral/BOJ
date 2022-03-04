m = int(input())
r = 0
table = [m]

while True:
    if len(table) == m:
        break
    t = table[-1]
    table.pop()
    t_ = t // 2

    if t % 2:
        table.append(t_)
        table.append(t_ + 1)
        r_ = (t_ + 1) * t_
    else:
        table.append(t_)
        table.append(t_)
        r_ = t_ * t_
    
    r += r_
    table.sort()

print(r)
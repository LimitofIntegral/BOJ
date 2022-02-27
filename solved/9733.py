d = {"Re" : 0, "Pt" : 0, "Cc" : 0, "Ea" : 0, "Tb" : 0, "Cm" : 0, "Ex" : 0}
t = 0

while True:
    try:
        a = input().split()
        for i in a:
            t += 1
            if i in d:
                d[i] += 1
    except EOFError:
        break


for i in d:
    print(str(i) + " " + str(d[i]) + " {:.2f}".format(d[i] / t, 2))

print("Total " + str(t) + " 1.00")

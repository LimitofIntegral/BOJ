import sys
input = sys.stdin.readline

win1 = [['P', 'R'], ['S', 'P'], ['R', 'S']]
win2 = [['R', 'P'], ['P', 'S'], ['S', 'R']]

for _ in range(int(input())):
    p1, p2 = 0, 0
    n = int(input())
    for i in range(n):
        a = input().split()
        if a in win1:
            p1 += 1
        elif a in win2:
            p2 += 1
    
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")
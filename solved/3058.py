for _ in range(int(input())):
    a = [i for i in list(map(int, input().split())) if not i % 2]
    print(sum(a), min(a))
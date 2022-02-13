class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    

n = int(input())
arr = list(map(int, input().split()))


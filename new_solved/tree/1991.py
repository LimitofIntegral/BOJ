class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def init(node, data):
    if node:
        if node.data == data[0]:
            if data[1] != ".":
                node.left = Node(data[1])
            if data[2] != ".":
                node.right = Node(data[2])
            
            return
        else:
            init(node.left, data)
            init(node.right, data)


def pre(node):
    if node:
        print(node.data, end = "")
        pre(node.left)
        pre(node.right)


def mid(node):
    if node:
        mid(node.left)
        print(node.data, end = "")
        mid(node.right)


def post(node):
    if node:
        post(node.left)
        post(node.right)
        print(node.data, end = "")

n = int(input())

node, left, right = input().split()

root = Node(node)
if left != ".":
    root.left = Node(left)
if right != ".":
    root.right = Node(right)

for _ in range(n - 1):
    init(root, input().split())

pre(root)
print()
mid(root)
print()
post(root)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find(node, n):
    if node:
        if node.left == n:
            return node, 0
        elif node.right == n:
            return node, 1
        else:
            find(node.left, n)
            find(node.right, n)

    
def preorder(node, n):
    if node:
        if node.data == n:
            return node
        else:
            preorder(node.left, n)
            preorder(node.right, n)

def find_leaf(node):
    if node:
        if node.left == None and node.right == None:
            return 1
        else:
            result += find_leaf(node.left)
            result += find_leaf(node.right)
            return result




n = int(input())
arr = list(map(int, input().split()))
d = int(input())

node_arr = []

for i in range(n):
    node_arr.append((arr[i], i)) # i는 노드번호

node_arr.sort()

for i in node_arr:
    if i[0] == -1:
        root = Node(i[1])
    else:
        node = preorder(root, i[1])
        if node:
            if node.left:
                node.right = Node(i[1])
            else:
                node.left = Node(i[1])

node_ = find(root, d)
print(node_)
if node_[1]:
    node_[0].right = None
else:
    node_[1].left = None

print(find_leaf(root))



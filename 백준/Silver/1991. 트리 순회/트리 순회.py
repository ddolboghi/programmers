n = int(input())
tree = {}
for _ in range(n):
    r, ln, rn = input().split()
    tree[r] = [ln, rn]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

root = 'A'
preorder(root)
print()
inorder(root)
print()
postorder(root)
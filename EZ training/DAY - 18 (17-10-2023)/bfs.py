class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
root=Node(1)
root.left=Node(2)
root.right=Node(3)

q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.val)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)    
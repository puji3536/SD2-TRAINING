class Node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    printing(root.left)
    printing(root.val)
    printing(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
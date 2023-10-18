#ques.94
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root):    
            if root==None:
                return 
            else:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
            return l
        return inorder(root)

#ques.144
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def preorder(root):    
            if root==None:
                return 
            else:
                l.append(root.val)
                preorder(root.left)
                preorder(root.right)
            return l
        return preorder(root)

#ques.145
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder(root):
            if root==None:
                return
            else:
                postorder(root.left)
                postorder(root.right)
                l.append(root.val)
            return l
        return postorder(root)
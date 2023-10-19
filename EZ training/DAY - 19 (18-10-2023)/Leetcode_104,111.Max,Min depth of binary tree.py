#MAX DEPTH OF BINARY TREE
class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
#MIN DEPTH OF BINARY TREE
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        if root.left==None or root.right==None:
            return 1+max(self.minDepth(root.left),self.minDepth(root.right))
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
    
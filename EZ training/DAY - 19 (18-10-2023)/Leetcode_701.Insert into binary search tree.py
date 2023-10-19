class Solution(object):
    def insertIntoBST(self, root, val):
        if root==None:
            root=TreeNode(val)
            return root
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        else:
            root.left=self.insertIntoBST(root.left,val)
        return root
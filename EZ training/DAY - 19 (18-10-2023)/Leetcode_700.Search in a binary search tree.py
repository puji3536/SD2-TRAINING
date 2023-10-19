class Solution(object):
    def searchBST(self, root, val):
        if root==None:
            return
        if root.val==val:
            return root
        elif val>root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)  
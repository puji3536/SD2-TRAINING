class Solution(object):
    def sortedArrayToBST(self, nums):
        def fun(si,li):
            if si<=li:
                mid=(si+li)//2
                root=TreeNode(nums[mid])
                root.left=fun(si,mid-1)
                root.right=fun(mid+1,li)
                return root
        return fun(0,len(nums)-1)
        
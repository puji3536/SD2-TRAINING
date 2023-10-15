class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        l=0
        i=0
        r=len(nums)-1
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i]==1:
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1

        
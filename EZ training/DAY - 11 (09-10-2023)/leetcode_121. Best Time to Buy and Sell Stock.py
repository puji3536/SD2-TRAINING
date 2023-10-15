class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
       
        max1=0
        for i in prices:
            if (min1>i):
                min1=i
            elif(i-min1)>max1:
                max1=i-min1
        return max1

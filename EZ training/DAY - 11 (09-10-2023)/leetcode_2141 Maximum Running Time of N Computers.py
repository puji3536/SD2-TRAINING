class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total=sum(batteries)
        while batteries[-1]>total//n:
            total-=batteries[-1]
            batteries.pop()
            n-=1
        return total//n

class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        d={i:[] for i in range(n)}
        for i in p:
            d[i[0]].append(i[1])
        def dfs(start,vis):
            if start in vis:
                return False
            if d[start]==[]:
                return True
            vis.append(start)
            for i in d[start]:
                if dfs(i,vis)==False:
                    return False
            vis.remove(start)
            d[start]=[]
            return True
        for i in d:
            if dfs(i,[])==False:
                return False
        return True
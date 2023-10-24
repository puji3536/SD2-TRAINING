class Solution(object):
    def allPathsSourceTarget(self, graph):
        ans=[]
        def dfs(start,end,visited):
            if start==end:
                val=visited+[start]
                ans.append(val)
                return
            visited.append(start)
            for i in graph[start]:
                if i not in visited:
                    dfs(i,end,visited)
            visited.pop()
        dfs(0,len(graph)-1,[])
        return ans
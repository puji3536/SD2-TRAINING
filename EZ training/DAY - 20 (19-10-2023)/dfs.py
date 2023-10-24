def fun(d,start,vis):
    def dfs(start,vis):
        vis.add(start)
        for i in d[start]:
            if i not in vis:
                dfs(i,vis)
        return vis
    return dfs(start,vis)
d={1:[2],2:[3,5],3:[5],4:[2,3],5:[]}
start=1
vis=set()
print(fun(d,start,vis))
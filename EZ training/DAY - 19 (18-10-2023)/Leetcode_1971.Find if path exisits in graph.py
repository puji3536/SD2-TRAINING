class Solution(object):
    def validPath(self, n, edges, source, destination):
        if not edges:
            return True
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        q=[source]
        vis=set()
        while q:
            a=q.pop(0)
            for i in d[a]:
                if i==destination:
                    return True
                if i not in vis:
                    q.append(i)
                    vis.add(i)
        return False    
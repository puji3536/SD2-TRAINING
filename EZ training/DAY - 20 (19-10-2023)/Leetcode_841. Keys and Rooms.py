class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: 
        vis=set()
        def dfs(start):
            vis.add(start)
            for i in rooms[start]:
                if i not in vis:
                    dfs(i)
        dfs(0)
        return True if len(vis)==len(rooms) else False
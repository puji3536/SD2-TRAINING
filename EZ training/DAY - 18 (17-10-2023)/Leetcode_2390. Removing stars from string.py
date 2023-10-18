from collections import deque
class Solution(object):
    def removeStars(self, s):
        st=[]
        for i in s:
            if i=='*':
                st.pop()
            else:
                st.append(i)
        return "".join(st)
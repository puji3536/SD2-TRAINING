from collections import deque
class Solution(object):
    def minLength(self, s):
        st=deque()
        for i in s:
            if not st:
                st.append(i)
            elif i=='B' and st[-1]=='A':
                st.pop()
            elif i=='D' and st[-1]=='C':
                st.pop()
            else:
                st.append(i)
        return len(st)
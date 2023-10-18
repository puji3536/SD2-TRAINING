from collections import deque
class Solution(object):
    def removeDuplicates(self, s):
        st=collections.deque()
        for i in s:
            if not st:
                st.append(i)
            elif i==st[-1]:
                st.pop()
            else:
                st.append(i)
        return "".join(st)   
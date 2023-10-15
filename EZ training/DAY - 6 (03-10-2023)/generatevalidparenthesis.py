class Solution(object):
    def generateParenthesis(self, n):
        l = []
        res = []

        def backtrack(opencount=0, closecount=0):
            if opencount == closecount == n:
                res.append("".join(l))
            if opencount < n:
                l.append('(')
                backtrack(opencount + 1, closecount)
                l.pop()
            if closecount < opencount:
                l.append(')')
                backtrack(opencount, closecount + 1)
                l.pop()
            return res

        return backtrack()

if _name_ == "_main_":
    n = int(input("Enter the value of n: "))
    solution = Solution()
    result = solution.generateParenthesis(n)
    print("Generated Parentheses:", result)
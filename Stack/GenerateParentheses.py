class Solution:
    def generateParenthesis(self, n: int):
        stack = []
        res = []

        def backingTracking(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backingTracking(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backingTracking(open, close + 1)
                stack.pop()
        backingTracking(0, 0)
        return res


obj = Solution()
print(obj.generateParenthesis(3))

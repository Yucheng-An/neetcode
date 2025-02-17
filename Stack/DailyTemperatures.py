class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([i, t])
        return res

obj = Solution()
# temperatures = [30, 38, 30, 36, 35, 40, 28]
temperatures = [22,21,20]
print(obj.dailyTemperatures(temperatures))

class Solution:
    def carFleet(self, target, position, speed):
        pair = []
        stack = []
        for i in (range(len(position))):
            pair.append((position[i], speed[i]))
        pair.sort(reverse=True)
        print(pair)
        for p, s in pair:
            finishTime = (target - p) / s
            stack.append(finishTime)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]
obj = Solution()
print(obj.carFleet(target, position, speed))

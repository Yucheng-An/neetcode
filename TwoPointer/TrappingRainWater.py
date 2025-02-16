class Solution:
    """
    O(n) time O(n) space
    """
    def trap(self, height):
        leftMaxList = []
        leftMax = 0
        for i in range(len(height)):
            leftMaxList.append(leftMax)
            leftMax = max(leftMax, height[i])
        rightMaxList = []
        rightMax = 0
        for i in range(len(height) - 1, -1, -1):
            rightMaxList.append(rightMax)
            rightMax = max(rightMax, height[i])
        rightMaxList.reverse()
        res = 0
        for i in range(len(height)):
            if min(leftMaxList[i], rightMaxList[i]) - height[i] > 0:
                res += min(leftMaxList[i], rightMaxList[i]) - height[i]
        return res
class Solution2:
    """
    O(n) time O(1) space using two pointer
    """
    def trap(self, height):
        left , right = 0, len(height)-1
        leftmax = height[left]
        rightmax = height[right]
        res = 0
        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax,height[left])
                res += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax,height[right])
                res += rightmax - height[right]
        return res
        


obj = Solution2()
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
print(obj.trap(height))

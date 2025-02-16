class Solution:
    def maxArea(self, heights):
        left = 0
        right = len(heights) -1
        maxArea = 0
        while left < right:
            currentArea = min(heights[left],heights[right]) * (right - left)
            maxArea = max(maxArea,currentArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
    
obj = Solution()
height = [1,7,2,5,4,7,3,6]
print(obj.maxArea(height))

                
        
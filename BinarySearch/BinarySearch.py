class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return -1


obj = Solution()
nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(obj.search(nums, target))

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res


obj = Solution()
nums = [3, 4, 5, 6, 1, 2]
print(obj.findMin(nums))

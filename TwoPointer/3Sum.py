"""
This is very important concept!
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.twoSumPair(nums[i+1:],-nums[i])
            for pair in pairs:
                res.append([nums[i]] + pair)
        return res
            

    def twoSumPair(self, nums, target):
        pair = []
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                pair.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif sum > target:
                right -= 1
            else:
                left += 1
        return pair


nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))

class Solution:
    def twoSum(nums, target):
        relatedmap = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in relatedmap:
                return [relatedmap[need], i]
            else:
                relatedmap[nums[i]] = i
        return []


nums = [3, 4, 5, 6]
target = 7
obj = Solution()
print(obj.twoSum(nums))

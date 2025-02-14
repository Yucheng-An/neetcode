class Solution:
    def hasDuplicate(self, nums):
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = 1
        return False
class Solution:
    def longestConsecutive(self, nums):
        """
        Input: nums = [2,20,4,10,3,4,5]
        """
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(length,longest)
        return longest


nums = [2,20,4,10,3,4,5]
obj = Solution()
print(obj.longestConsecutive(nums))
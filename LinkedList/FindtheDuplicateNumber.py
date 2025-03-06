class Solution:
    def findDuplicate(self, nums):
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        newslow = 0
        while True:
            newslow = nums[newslow]
            if slow == newslow:
                return slow

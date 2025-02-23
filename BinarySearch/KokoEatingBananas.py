import math


class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        res = float("inf")
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res


obj = Solution()
# piles = [1, 4, 3, 2]
# h = 9
piles = [25,10,23,4]
h = 4
print(obj.minEatingSpeed(piles, h))

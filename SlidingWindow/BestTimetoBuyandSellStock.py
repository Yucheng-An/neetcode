class Solution:
    def maxProfit(self, prices):
        res = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[right] > prices[left]:
                res = max(res, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return res


obj = Solution()
prices = [10, 1, 5, 6, 7, 1]
print(obj.maxProfit(prices))

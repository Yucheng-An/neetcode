class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


s = "XQYAXSADAWSDX"
k = 5
obj = Solution()
print(obj.characterReplacement(s, k))

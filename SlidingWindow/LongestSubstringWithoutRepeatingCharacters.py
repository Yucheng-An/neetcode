class Solution:
    def lengthOfLongestSubstring(self, s: str):
        myset = set()
        left = 0
        right = 0
        res = 0
        while right < len(s):
            while s[right] in myset:
                myset.remove(s[left])
                left += 1
            myset.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res


obj = Solution()
s = "zxyzxyz"
print(obj.lengthOfLongestSubstring(s))

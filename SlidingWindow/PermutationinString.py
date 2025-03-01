class Solution:
    def checkInclusion(self, s1: str, s2: str):
        s1Map = {}
        for c in s1:
            if c in s1Map:
                s1Map[c] += 1
            else:
                s1Map[c] = 1
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            tmap = {}
            for i in range(left, right +1):
                if s2[i] in tmap:
                    tmap[s2[i]] += 1
                else:
                    tmap[s2[i]] = 1
            if tmap == s1Map:
                return True
            left += 1
            right += 1
        return False

# s1 = "abc"
# s2 = "lecabee"

s1="ab"
s2="eidboaoo"
obj = Solution()
print(obj.checkInclusion(s1, s2))

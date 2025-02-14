class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mymap = {}
        for i in range(len(s)):
            if s[i] not in mymap:
                mymap[s[i]] = 1
            else:
                mymap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in mymap or mymap[t[i]] ==0:
                return False
            else:
                mymap[t[i]] -= 1
        return True
    
    
s = "racecar"
t = "carrace"
object = Solution()
print(object.isAnagram(s,t))
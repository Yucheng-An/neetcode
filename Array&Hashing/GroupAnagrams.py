class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())


strs = ["act", "pots", "tops", "cat", "stop", "hat"]
obj = Solution()
print(obj.groupAnagrams(strs))

import heapq
class Solution:
    def topKFrequent(self, nums,k):
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        heaplist = []
        for num in hashmap.keys():
            heapq.heappush(heaplist,(hashmap[num],num))
            if len(heaplist) > k:
                heapq.heappop(heaplist)
        print(heaplist)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heaplist)[1])
        return res
            



nums = [100,100,100,100,100,20,20,30,30,30]
obj = Solution()
print(obj.topKFrequent(nums,2))
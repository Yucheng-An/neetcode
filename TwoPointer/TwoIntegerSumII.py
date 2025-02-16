class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) -1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                return [left+1,right+1]
        return []

numbers = [1,2,3,4]
target = 3
obj = Solution()
print(obj.twoSum(numbers,target))

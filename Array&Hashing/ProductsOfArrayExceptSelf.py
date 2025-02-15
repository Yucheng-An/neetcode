class Solution:
    def productExceptSelf(self, nums):
        leftProduct = [1] * len(nums)
        for i in range(1, len(nums)):
            leftProduct[i] = nums[i - 1] * leftProduct[i - 1]
        print(leftProduct)
        print(f"should be [1,1,2,8]")
        rightProduct = [1] * len(nums)
        for i in range(len(rightProduct) - 2, -1, -1):
            rightProduct[i] = nums[i + 1] * rightProduct[i + 1]
        print(rightProduct)
        print(f"should be [48,24,6,1]")
        res = []
        for i in range(len(nums)):
            res.append(int(leftProduct[i] * rightProduct[i]))
        return res
            

obj = Solution()
nums = [1, 2, 4, 6]
print(obj.productExceptSelf(nums))


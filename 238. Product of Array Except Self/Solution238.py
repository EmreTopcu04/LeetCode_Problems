class Solution(object):
    def productExceptSelf(self, nums):

        leftMultiplier = 1
        rightMultiplier = 1
        length = len(nums)
        ans = [0] * length
        leftArray = [0] * length
        rightArray = [0] * length
        
        for i in range(length):

            j = -i - 1
            leftArray[i] = leftMultiplier
            rightArray[j] = rightMultiplier
            leftMultiplier *= nums[i]
            rightMultiplier *= nums[j]
        
        for i in range(length):
            ans[i] = leftArray[i] * rightArray[i]
            
        return ans

c = Solution()



print(c.productExceptSelf([1,2,3,4]))
        

        
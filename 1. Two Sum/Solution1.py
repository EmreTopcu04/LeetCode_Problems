class Solution(object):
    def twoSum(self, nums:list, target:list):
       
        ans = []
        ourMap = dict()
        for i in range(len(nums)):
            ourMap[nums[i]] = i
        
        for i in range(len(nums)):
            otherKey = target - nums[i]
            if ourMap.keys().__contains__(otherKey) and ourMap[otherKey] != i:
                ans.append(i)
                ans.append(ourMap[otherKey])
                break
        return ans
    
c = Solution()

print(c.twoSum([3,2,4],6))
class Solution(object):
    def majorityElement(self, nums:list):
       
        ourMap = {}
        size = len(nums)
        index = 0
        max_value = size/2

        for num in nums:

            if ourMap.__contains__(num):
                ourMap[num] += 1
            else:
                ourMap[num] = 1

        for i in ourMap.keys():
            if (ourMap[i] > max_value):
                ourMap[i] = max_value
                index = i
        return index

        

c = Solution()

print(c.majorityElement([2,2,1,1,1,2,2]))
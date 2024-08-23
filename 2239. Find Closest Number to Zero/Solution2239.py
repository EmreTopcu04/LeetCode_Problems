class Solution2239(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for i in range(len(nums)):
            if (abs(nums[i]) < abs(closest)):
                closest = nums[i]
        if (closest < 0 and abs(closest) in nums):
            return abs(closest)
        else:
            return closest
        

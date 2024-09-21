class Solution(object):
    def threeSum(self, nums:list):

        nums.sort()
        size = len(nums)
        ans = []

        for i in range(size):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            left,right = i+1,size-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left, right = left+1,right-1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans


c = Solution()
print(c.threeSum([-1,0,1,2,-1,-4]))
class Solution(object):
    def sortedSquares(self, nums:list):
        left = 0
        right = len(nums) - 1
        ans = []

        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                ans.append(nums[right]**2)
                right -= 1
            elif nums[left] ** 2 > nums[right] ** 2:
                ans.append(nums[left]**2)
                left += 1
            else:
                ans.append(nums[left]**2)
                left += 1

        ans.reverse()

        return ans


c = Solution()

print(c.sortedSquares([-7,-3,2,3,11]))
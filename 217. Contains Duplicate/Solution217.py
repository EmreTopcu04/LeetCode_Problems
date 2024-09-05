class Solution(object):
    def containsDuplicate(self, nums: list):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = set(nums)
        return len(ans) != len(nums)
        

c = Solution()

print(c.containsDuplicate([1,2,3,4]))
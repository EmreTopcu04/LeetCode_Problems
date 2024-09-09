class Solution(object):
    def longestConsecutive(self, nums:list):
        
        ourSet = set(nums)
        max_sequence = 0
        for num in nums:
            if num-1 not in ourSet:
                next_num = num + 1
                sequence = 1
                while next_num in ourSet:
                    sequence += 1
                    next_num += 1
                max_sequence = max(max_sequence,sequence)

        return max_sequence


c = Solution()
print(c.longestConsecutive([100,4,200,1,3,2]))
        
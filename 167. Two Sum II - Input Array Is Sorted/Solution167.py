class Solution(object):
    def twoSum(self, numbers:list, target:int):
        left = 0
        right = len(numbers) - 1

        while left <= right:
            number = numbers[left] + numbers[right]
            if number > target:
                right -= 1
            elif number < target:
                left += 1
            else:
                return [left+1,right+1]



c = Solution()

print(c.twoSum([2,4,5,6,7,12,15], 10))
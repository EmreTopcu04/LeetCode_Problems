class Solution(object):
    def maxArea(self, height:list):
        max_area = 0
        left, right = 0,len(height) - 1
        while left <= right:
            area = (right-left)*min(height[left],height[right])
            if (area > max_area):
                max_area = area
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return max_area

c = Solution()

print(c.maxArea([1,8,6,2,5,4,8,3,7]))
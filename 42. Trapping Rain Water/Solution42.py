class Solution(object):
    def trap(self, height:list):
        left_wall,right_wall = 0,0
        size = len(height)
        max_left = [0] * size
        max_right = [0] * size

        for i in range(size):
            j = -i-1
            max_left[i] = left_wall
            max_right[j] = right_wall
            left_wall = max(left_wall,height[i])
            right_wall = max(right_wall,height[j])

        total = 0
        for i in range(size):
            pot = min(max_left[i],max_right[i])
            total += max(0,pot-height[i])
        
        return total

c = Solution()

print(c.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
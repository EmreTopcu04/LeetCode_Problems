class Solution(object):
    def reverseString(self, s:list):
        
        left = 0
        right = len(s)-1

        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1


        

c = Solution()

print(c.reverseString(["h","e","l","l","o"]))
class Solution(object):
    def isPalindrome(self, s:str):
        s = ''.join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(s) - 1


        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
c = Solution()

print(c.isPalindrome("A man, a plan, a canal: Panama"))
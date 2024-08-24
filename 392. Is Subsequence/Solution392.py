class Solution(object):
    def isSubsequence(self, s, t):
        for i in range(len(t)):
            
            if len(s) == 0:
                break;
            if s[0] == t[i]:
                
                s = s[1:]
                
        return len(s) == 0

c = Solution()
print (c.isSubsequence("axc","ahbgdc"))          
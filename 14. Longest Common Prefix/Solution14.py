class Solution(object):
    def longestCommonPrefix(self, strs):
        min = float("inf")
        for string in strs:
            if len(string) < min:
                min = len(string)
        
        i = 0
        while i < min:
            for string in strs:
                if (string[i] != strs[0][i]):
                    return string[:i]
            i += 1
        return strs[0][:i]    


c = Solution()

print(c.longestCommonPrefix([["flower","flow","flight"]]))
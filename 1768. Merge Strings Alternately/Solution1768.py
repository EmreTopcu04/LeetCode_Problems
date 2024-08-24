class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        minimum = min(len(word1),len(word2))
        string = ""
        for x in range(minimum):
            string += word1[x]
            string += word2[x]
   
        if len(word1) > len(word2):
            string += word1[minimum:]
        else:
            string += word2[minimum:]
        return string
    
c = Solution()
print (c.mergeAlternately("abc","pqr"))       
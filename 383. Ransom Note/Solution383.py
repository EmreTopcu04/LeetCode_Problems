class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        letters = {}
        for i in range(len(magazine)):
            if letters.__contains__(magazine[i]):
                count = letters.get(magazine[i])
                letters[magazine[i]] = count+1    
            else:
                letters[magazine[i]] = 1    

        for i in range(len(ransomNote)):
            if (letters.keys().__contains__(ransomNote[i])):
                count = letters.get(ransomNote[i])
                letters[ransomNote[i]] = count - 1
                if letters[ransomNote[i]] == 0:
                    letters.pop(ransomNote[i])
            else:
                return False
        return True
c = Solution()

print(c.canConstruct("aa","ab"))
class Solution(object):
    def isAnagram(self, s, t):
       
        letters_1 = {}
        letters_2 = {}

        for i in range(len(s)):
            if letters_1.__contains__(s[i]):
                letters_1[s[i]] += 1
            else:
                letters_1[s[i]] = 1
        
        for i in range(len(t)):
            if letters_2.__contains__(t[i]):
                letters_2[t[i]] += 1
            else:
                letters_2[t[i]] = 1
        
        return letters_1 == letters_2

c = Solution()

print(c.isAnagram("rat","car"))
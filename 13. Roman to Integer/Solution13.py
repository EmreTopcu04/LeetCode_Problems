class Solution(object):
    def romanToInt(self, s):        
       romanMap = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
       sum = 0
       length = len(s)
       i = 0
       while i < length:
            if i < length - 1 and romanMap[s[i]] < romanMap[s[i+1]]:
                sum += romanMap[s[i+1]] - romanMap[s[i]]
                i += 2
            else:
                sum += romanMap[s[i]]
                i += 1
       return sum
    
c = Solution()
print (c.romanToInt("MCMXCIV"))       
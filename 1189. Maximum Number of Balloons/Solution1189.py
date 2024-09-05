class Solution(object):
    def maxNumberOfBalloons(self, text:str):
        
        counter = {}
        balloon = "balloon"
        
        for c in text:
            if c in balloon:
                if counter.__contains__(c):
                    counter[c] += 1
                else:
                    counter[c] = 1 
                       
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter["b"],counter["a"],counter["l"]//2,counter["o"]//2,counter["n"])

c = Solution()

print(c.maxNumberOfBalloons("nlaebolko"))
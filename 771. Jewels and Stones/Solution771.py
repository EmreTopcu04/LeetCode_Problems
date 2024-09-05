class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        ans = 0
        jewelSet = set(jewels)
        
        for i in range(len(stones)):
            if jewelSet.__contains__(stones[i]):
                ans += 1

        return ans

c = Solution()

print(c.numJewelsInStones("z","ZZ"))
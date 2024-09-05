class Solution(object):
    def groupAnagrams(self, strs: list):
        ans = {}
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            
            if sorted_word in ans:
                ans[sorted_word].append(word)
            else:
                ans[sorted_word] = [word]
        
        return list(ans.values())
    

c = Solution()

print(c.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
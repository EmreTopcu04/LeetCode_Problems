class Solution(object):
    def isValid(self, s:str):
        stk = []
        paranthesis = {'{':'}','[':']','(':')'}
        for c in s: 
            if stk:
                if c == paranthesis[stk[-1]]:
                    stk.pop()
                else:
                    if c in paranthesis.keys():
                        stk.append(c)
                    else:
                        return False

            else:
                if c in paranthesis.keys():
                    stk.append(c)
                else:
                    return False

        return len(stk) == 0
        
c = Solution()

print(c.isValid("(])"))
        
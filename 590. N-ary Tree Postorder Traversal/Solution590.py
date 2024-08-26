class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        
        if not root:
            return []
        
        ans = []

        def dfs(root):

            for node in root.children:
                dfs(node)

            ans.append(root.val)

        dfs(root)

        return ans
        
            
        
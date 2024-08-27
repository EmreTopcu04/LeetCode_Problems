class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        dist = [0] * n
        dist[start_node] = 1
        
        
        for index in range(n-1):
            flag = False
            for node, (start,end) in enumerate(edges):
                if dist[start] * succProb[node] > dist[end]:
                    dist[end] = dist[start] * succProb[node]
                    flag = True 
                if dist[end] * succProb[node] > dist[start]:
                    dist[start] = dist[end] * succProb[node]
                    flag = True
            
            if not flag:
                break
                
                    
        return dist[end_node]

c = Solution()

print(c.maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.2],0,2))
        
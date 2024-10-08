class Solution(object):
    def rotate(self, matrix):
 
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

        return matrix
        

c = Solution()

print(c.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
))
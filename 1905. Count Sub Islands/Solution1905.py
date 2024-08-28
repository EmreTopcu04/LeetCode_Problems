class Solution(object):
    def countSubIslands(self, grid1, grid2):
        rows , cols = len(grid1), len(grid1[0])
        visit = set()

        def dfs(row,column):
           
            if (row < 0 or column < 0 or row == rows or column == cols or grid2[row][column] == 0 or (row,column) in visit):
                return True
            
            visit.add((row,column))
            result = True
            
            if (grid1[row][column] == 0):
                result = False

            result = dfs(row-1,column) and result
            result = dfs(row+1,column) and result
            result = dfs(row,column-1) and result
            result = dfs(row,column+1) and result
            
            return result


        count = 0
        for row_i in range(rows):
            for col_i in range(cols):
                if (grid2[row_i][col_i] == 1 and (row_i,col_i) not in visit and dfs(row_i,col_i)):
                    count += 1

        return count
        
c = Solution()

print(c.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
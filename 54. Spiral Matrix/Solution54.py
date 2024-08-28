class Solution(object):
    def spiralOrder(self, matrix):
        
        list = []

        row,col = len(matrix),len(matrix[0])

        UP,RIGHT,DOWN,LEFT = 0,1,2,3
        
        i,j = 0,0

        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = col
        DOWN_WALL = row
        LEFT_WALL = -1  

        while len(list) != col*row:

            if direction == RIGHT:
                
                while j < RIGHT_WALL:
                    list.append(matrix[i][j])
                    j += 1

                i,j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN
                
            elif direction == DOWN:

                while i < DOWN_WALL:
                    list.append(matrix[i][j])
                    i += 1
                i,j = i-1 , j-1
                DOWN_WALL = DOWN_WALL - 1
                direction = LEFT

            elif direction == LEFT:
                
                while j > LEFT_WALL:
                    list.append(matrix[i][j])
                    j -= 1

                i,j = i-1, j+1

                LEFT_WALL = LEFT_WALL + 1
                direction = UP

            else:

                while i > UP_WALL:
                    list.append(matrix[i][j])
                    i -= 1

                i,j = i+1,j+1
                UP_WALL = UP_WALL + 1
                direction = RIGHT

        return list

c = Solution()

print(c.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
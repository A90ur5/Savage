class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lenX, lenY = len(matrix[0]), len(matrix)
        res = [0] * (lenX * lenY)
        edge_right, edge_down, edge_left, edge_up = lenX-1, lenY-1, 0, 0
        x, y = 0, 0

        #direction: X_toRight:0 Y_toDown:1 X_toLeft:2 Y_toUp:3
        if lenX == 1:
            direction = 1
        else:
            direction = 0 
            
        for i in range(lenX * lenY):
            res[i] = matrix[y][x]

            if direction == 0:
                x += 1
                if x == edge_right:
                    direction = 1
                    edge_up += 1

            elif direction == 1:
                y += 1
                if y == edge_down:
                    direction = 2
                    edge_right -= 1
            
            elif direction == 2:
                x -= 1
                if x == edge_left:
                    direction = 3
                    edge_down -= 1
            
            elif direction == 3:
                y -= 1
                if y == edge_up:
                    direction = 0
                    edge_left += 1
        
        return res


"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[]]
        
        right = n # cols
        left = 0
        bottom = n # rows
        top = 0
        
        spiral = [[0 for i in range(n)] for j in range(n)]
        j = 1
        
        while j <= n**2:
            if top >= bottom or left >=right:
                break
            #Traversing top row
            for i in range(left,right):
                spiral[top][i] = j
                # print((top,i))
                j = j+1
                # spiral.append(matrix[top][i])
                
            top = top+1
            
            if top >= bottom or left >= right:
                break
            #Traversing right most column
            for i in range(top, bottom):
                spiral[i][right-1] = j
                # spiral.append(matrix[i][right-1])
                j = j+1
            
            right = right-1

            if top >= bottom or left >=right:
                break
            #Traversing bottom row in reverse
            for i in range(right,left, -1):
                spiral[bottom-1][i-1] = j
                # spiral.append(matrix[bottom-1][i-1])
                j = j+1
            
            bottom = bottom-1
            
            if top >= bottom or left >=right:
                break
            # Traversing left most column in reverse
            for i in range(bottom, top, -1):
                # pass
                spiral[i-1][left] = j
                # spiral.append(matrix[i-1][left])
                j = j+1
            
            left = left+1


        return spiral
           

        
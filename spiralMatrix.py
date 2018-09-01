"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        right = len(matrix[0]) # cols
        left = 0
        bottom = len(matrix) # rows
        top = 0
        
        spiral = []
        
        
        while left<=right or top<=bottom:
            if top >= bottom or left >=right:
                break
            #Traversing top row
            for i in range(left,right):
                # print((top,i))
                spiral.append(matrix[top][i])
                
            top = top+1
            
            if top >= bottom or left >= right:
                break
            #Traversing right most column
            for i in range(top, bottom):
                # print((i, right-1))
                spiral.append(matrix[i][right-1])
            
            right = right-1

            if top >= bottom or left >=right:
                break
            #Traversing bottom row in reverse
            for i in range(right,left, -1):
                # print((bottom-1, i-1))
                spiral.append(matrix[bottom-1][i-1])
            
            bottom = bottom-1
            
            if top >= bottom or left >=right:
                break
            # Traversing left most column in reverse
            for i in range(bottom, top, -1):
                # pass
                # print((i-1, left))
                spiral.append(matrix[i-1][left])
            
            left = left+1


        return spiral
           

        
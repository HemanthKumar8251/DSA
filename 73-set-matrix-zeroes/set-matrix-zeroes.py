class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Space Complexity O(m+n)
        # rows = set()
        # columns = set()
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #             rows.add(i)
        #             columns.add(j)
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in columns:
        #             matrix[i][j]=0

        # Space Complexity O(1)
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = False        
        first_col_has_zero = False

        # check if the first row contains zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check if the first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # use the first row and column as a note
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # set the marked rows to zero
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        # set the marked columns to zero
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
    
        # set the first row to zero if needed
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # set the first column to zero if needed
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
        
        return matrix
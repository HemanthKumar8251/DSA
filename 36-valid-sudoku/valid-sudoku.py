class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # O(9*9) Time - Constant Time, O(3*9*9) - Constant Space
        # We can reduce space to O(3*3) but time complexity increases as we need to run
        # 9*9 loop 3 times 
        row_map = [[False]*9 for _ in range(9)]
        col_map = [[False]*9 for _ in range(9)]
        box_map = [[[False]*9 for _ in range(3)] for j in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    ele = int(board[i][j])
                    if row_map[i][ele-1] or col_map[j][ele-1] or box_map[i//3][j//3][ele-1]:
                        return False
                    row_map[i][ele-1] = True
                    col_map[j][ele-1] = True
                    box_map[i//3][j//3][ele-1] = True
        return True
            

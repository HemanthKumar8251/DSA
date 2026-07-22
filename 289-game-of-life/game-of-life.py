class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),  (0, 1), 
                  (1, -1),  (1, 0),  (1, 1)]
        m = len(board)
        n = len(board[0])
        # In place encrypting
        for i in range(m):
            for j in range(n):
                alive = 0
                for r,c in neighbours:
                    nr,nc = i+r,j+c
                    if 0<=nr<m and 0<=nc<n:
                        if board[nr][nc]%2==1:
                            alive += 1
                if board[i][j]==1 and alive in [2,3]:
                    board[i][j] = 3
                if board[i][j]==0 and alive==3:
                    board[i][j] = 2
        
        # Decrypting
        for i in range(m):
            for j in range(n):
                if board[i][j]==3:
                    board[i][j]=1
                elif board[i][j]==2:
                    board[i][j]=1
                else:
                    board[i][j]=0
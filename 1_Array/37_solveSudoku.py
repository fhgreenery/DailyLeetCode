class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.helper(board)
    
    def helper(self, board):
        num = len(board)
        for i in range(num):
            for j in range(num):
                if board[i][j] == '.':
                    for t in range(1,10):
                        c = str(t)
                        if self.is_valid(board, c, i, j):
                            board[i][j] = c
                            if self.helper(board):
                                return True
                            else:
                                board[i][j] = '.' 
                    return False  # The current insertion of 1~9 is invalid, and it goes back to the previous state
        return True  # When inserting the last number successfully, it needs to return True, so as to confirm the previous state
               
    def is_valid(self, board, c, row , col):
        num = len(board)
        # check row 
        for m in range(num):
            if board[row][m] == c:
                return False
                
        # check column 
        for n in range(num):
            if board[n][col] == c:
                return False
               
        # check block 
        row_start = (row//3)*3
        column_start = (col//3)*3
        for i in range(row_start,row_start+3):
            for j in range(column_start,column_start+3):
                if board[i][j] == c:
                    return False
        return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]

    s = Solution()
    print(s.helper(board)) 
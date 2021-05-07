class Solution:
    
    
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def isWinner(player: str, board: List[str]) -> bool:
        
            for c in range(0,2):
                if board[0][c] == board[1][c] == board[2][c] == player:
                    return True

            for r in range(0,2):
                if board[r].count(player) == 3:
                    return True

            if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
                return True
        
        x = 0
        o = 0
        for string in board:
            x += string.count('X')
            o += string.count('O')
        
        if isWinner('X', board):
            if isWinner('0', board):
                return False
        
        if isWinner('O', board) and x != o:
            return False
        
        if isWinner('X', board) and x-o !=1:
            return False
        
        
        if x + o == 9:
            return True
        
        if x+o == 8 and x == o and not isWinner("X", board) :
            return True
        
        if x-o <= 1 and x-o>-1:
            return True

        return False
        

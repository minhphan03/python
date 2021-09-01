class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # attempt by Kuman_Kothiya
        
        #check for duplicates
        def valid(arr):
            #since a set only return non-duplicates, compare length of set to the real array
            if len(arr) == len(set(arr)):
                return True
            return False
        
        #row validations
        for i in range(9):
            li = [board[i][j] for j in range(9) if board[i][j] != "."]
            if not valid(li):
                return False
        
        #column validations
        for j in range(9):
            li = [board[i][j] for i in range(9) if board[i][j] != "."]
            if not valid(li):
                return False
        
        #sub-boxes validations
        for i in range(0,9,3):
            for j in range(0,9,3):
                # nested loops: for k, for l
                block = [board[k][l] for k in range(i,i+3) for l in range(j, j+3) if board[k][l] != '.']
                if not valid(block):
                    return False
        
        return True

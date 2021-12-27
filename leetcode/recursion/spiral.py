class Solution:
    # recursive approach
    # algorithm explained by EnjoyAlgorithms

    # helper
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        height = len(matrix) - 1
        width = len(matrix[0]) - 1

        self.spiral(0, height, 0, width, matrix, res)
        return res

    def spiral(self, row1, row2, col1, col2, matrix, res):
        if (row1 > row2) or (col1 > col2):
            return

        # add first row
        for i in range(col1, col2 + 1):
            res.append(matrix[row1][i])

        # add last column
        for i in range(row1 + 1, row2+1):
            res.append(matrix[i][col2])

        # add last row if last and first column is not the same
        if row1 != row2:
            for i in range(col2 - 1, col1 - 1, -1):
                res.append(matrix[row2][i])

        # add first column if last and first row is not the same
        if col1 != col2:
            for i in range(row2 - 1, row1, -1):
                res.append(matrix[i][col1])

        # recursively call

        self.spiral(row1 + 1, row2 - 1, col1 + 1, col2 - 1, matrix, res)

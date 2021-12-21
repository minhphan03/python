#rotate 90 degrees clockwise for a 2D array matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # algorithm explained by Jack White on YouTube
        
        # first, transpose
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c] ,matrix[c][r]=matrix[c][r],matrix[r][c]
        
        # swap columns
        for c in matrix:
            c.reverse()

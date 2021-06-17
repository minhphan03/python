class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle_ = rectangle
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            if i >= len(self.rectangle_):
                self.rectangle_[i] = []
            for j in range(col1, col2+1):
                self.rectangle_[i][j] = newValue
        return

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle_[row][col]

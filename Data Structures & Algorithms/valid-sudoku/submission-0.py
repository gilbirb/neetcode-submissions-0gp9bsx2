class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            hsRow = {}
            hsCol = {}
            for j in range(9):
                numR = board[i][j]
                numC = board[j][i]
                if numR in hsRow and numR != ".":
                    return False
                if numC in hsCol and numC != ".":
                    return False
                hsRow[numR] = 1
                hsCol[numC] = 1

        def checkInBox(a, b):
            hs = {}
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    num = board[i][j]
                    if num in hs and num != ".":
                        return False
                    hs[num] = 1
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkInBox(i, j):
                    return False

        return True
                
        
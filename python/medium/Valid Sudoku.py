class Solution:
    #def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):
        rowSet = [set() for i in range(9)]
        columnSet = [set() for i in range(9)]
        boardSet = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                cur_value = board[i][j]
                if cur_value == '.':
                    continue
                if cur_value in ( rowSet[j] | columnSet[i] | boardSet[j//3 + (i//3)*3] ):
                    return False
                rowSet[j].add(cur_value)
                columnSet[i].add(cur_value)
                boardSet[j//3 + (i//3)*3].add(cur_value)
        return True



if __name__ == '__main__':
    ans = Solution()
    testData = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(ans.isValidSudoku(testData))
        
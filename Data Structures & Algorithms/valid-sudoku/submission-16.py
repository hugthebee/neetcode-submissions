class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        grid_set = [set() for _ in range(9)]

        for i, v1 in enumerate(board):
            for j, v2 in enumerate(board[i]):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row_set[i]:
                    return False

                if board[i][j] in col_set[j]:
                    return False
                print(i, j)
                if board[i][j] in grid_set[i//3 * 3 + j//3]:
                    return False

                # print(i, j)

                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                grid_set[i//3 * 3+ j//3].add(board[i][j])

        return True
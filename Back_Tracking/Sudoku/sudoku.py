def legal(board: list, x: int, y: int, n: int) -> bool:
    for i in range(9):
        if i == x:
            continue
        if board[y][i] == n:
            return False
    for j in range(9):
        if j == y:
            continue
        if board[j][x] == n:
            return False
    for k in range(9):
        i = (x // 3) * 3 + k % 3
        j = (y // 3) * 3 + k // 3
        if i == x and j == y:
            continue
        if board[j][i] == n:
            return False
    return True


def sudoku(board: list, x: int, y: int) -> bool:
    if y >= 9:
        return True
    elif x >= 9:
        return sudoku(board, 0, y + 1)
    else:
        if board[y][x] != 0:
            return sudoku(board, x + 1, y)
        for n in range(1, 10):
            if legal(board, x, y, n):
                board[y][x] = n
                if sudoku(board, x + 1, y):
                    return True
                else:
                    board[y][x] = 0
        return False


def main():
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    sudoku(board, 0, 0)
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()


main()

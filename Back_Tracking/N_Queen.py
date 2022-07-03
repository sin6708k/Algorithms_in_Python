# NxN 크기의 체스 보드가 주어 졌을 때, N개의 퀸이 서로 공격할 수 없는 지점에
# 배치할 수 있는 방법을 찾아라.
def n_queen(board) -> list:
    r = len(board)

    if r >= n:
        print(board)
        return

    for j in range(n):
        legal = True
        for i in range(r):
            if board[i] in (j, j + r - i, j - r + i):
                legal = False
                break
        if legal:
            n_queen(board + [j])


n = 4
n_queen(board=[])

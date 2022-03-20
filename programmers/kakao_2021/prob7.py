INF = 1e+10
N, M = 0, 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def is_finished(board, y, x):
    for y_diff, x_diff in zip(dy, dx):
        ny = y + y_diff
        nx = x + x_diff
        if in_range(ny, nx) and board[ny][nx] == 1:
            return False
    return True


def dfs(board, y1, x1, y2, x2):
    if is_finished(board, y1, x1):
        return False, 0
    if y1 == y2 and x1 == x2:
        return True, 1

    can_win = False
    min_count, max_count = INF, 0

    for y_diff, x_diff in zip(dy, dx):
        ny = y1 + y_diff
        nx = x1 + x_diff

        if (not in_range(ny, nx)) or board[ny][nx] != 1:
            continue

        board[y1][x1] = 0
        winlose, count = dfs(board, y2, x2, ny, nx)
        board[y1][x1] = 1

        if winlose:
            can_win = True
            min_count = min(min_count, count)
        elif not can_win:
            max_count = max(max_count, count)

    count = min_count if can_win else max_count
    return can_win, count


def solution(board, aloc, bloc):
    global N, M
    N = len(board)
    M = len(board[0])
    answer = dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]
    return answer


if __name__ == '__main__':
    board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    aloc = [1, 0]
    bloc = [1, 2]
    print(solution(board, aloc, bloc))
def solution(board, skill):
    answer = 0  # the number of preserved buildings
    width, height = len(board[0]), len(board)
    diff = [[0 for _ in range(width+1)] for _ in range(height+1)]

    # generate imos
    for tp, r1, c1, r2, c2, deg in skill:
        diff[r1][c1] += deg * (-1 if tp == 1 else 1)
        diff[r1][c2+1] += deg * (1 if tp == 1 else -1)
        diff[r2+1][c1] += deg * (1 if tp == 1 else -1)
        diff[r2+1][c2+1] += deg * (-1 if tp == 1 else 1)

    # calculate accumulative sum by row axis
    for cidx in range(height):
        asum = 0
        for ridx in range(width):
            diff[ridx][cidx] += asum
            asum = diff[ridx][cidx]

    # calculate accumulate sum by column axis
    for ridx in range(width):
        asum = 0
        for cidx in range(height):
            diff[ridx][cidx] += asum
            asum = diff[ridx][cidx]

    # calculate the number of buildings preserved
    for ridx, row in enumerate(board):
        for cidx, value in enumerate(row):
            value += diff[ridx][cidx]
            if value > 0: answer += 1

    return answer


if __name__ == '__main__':
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill))
def solution(board, skill):
    answer = 0  # the number of preserved buildings

    for ridx, row in enumerate(board):
        for cidx, value in enumerate(row):
            # iterate for each skills
            for tp, r1, c1, r2, c2, deg in skill:
                if (r1 <= ridx <= r2) and (c1 <= cidx <= c2):
                    if tp == 1: value -= deg
                    else: value += deg

            # check whether the building is preserved
            if value > 0: answer += 1

    return answer


if __name__ == '__main__':
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill))
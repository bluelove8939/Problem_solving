def solution(board, skill):
    answer = 0  # the number of preserved buildings

    # sort the skill array
    skill = sorted(skill, key=lambda x:(x[1], x[2], x[3], x[4]))

    for ridx, row in enumerate(board):
        for cidx, value in enumerate(row):

            # check whether the building is preserved
            if value > 0: answer += 1

    return answer


if __name__ == '__main__':
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill))
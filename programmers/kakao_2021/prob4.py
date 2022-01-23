def dfs(left, pivot, info, current):
    if pivot == len(info) - 1:
        # Calculate the score of each two players
        current[pivot] = left
        total_sc1, total_sc2 = 0, 0

        for idx, (sc1, sc2) in enumerate(zip(info, current)):
            if sc1 != 0 and sc1 >= sc2: total_sc1 += 10 - idx
            elif sc2 != 0 and sc2 > sc1: total_sc2 += 10 - idx

        if total_sc1 >= total_sc2:
            return [-1], -1
        return current, total_sc2 - total_sc1

    current_new = current[:]

    if left > info[pivot]:
        current_new[pivot] = info[pivot] + 1
        inc_res, inc_diff = dfs(left-info[pivot]-1, pivot+1, info, current_new)
        current_new[pivot] = 0
        exc_res, exc_diff = dfs(left, pivot+1, info, current_new)

        if exc_diff == -1 and inc_diff == -1:
            return [-1], -1
        elif inc_diff == exc_diff:
            for inc_val, exc_val in zip(reversed(inc_res), reversed(exc_res)):
                if inc_val == 1 and exc_val != 1:
                    return inc_res, inc_diff
                elif inc_val != 1 and exc_val == 1:
                    return exc_res, exc_diff
            return inc_res, inc_diff
        elif inc_diff > exc_diff:
            return inc_res, inc_diff
        else:
            return exc_res, exc_diff
    else:
        current_new[pivot] = 0
        exc_res, exc_diff = dfs(left, pivot+1, info, current_new)
        return exc_res, exc_diff


def solution(n, info):
    answer, diff = dfs(n, 0, info, [0]*len(info))
    return answer


# if __name__ == '__main__':
#     n = 5
#     info = 	[2,1,1,1,0,0,0,0,0,0,0]
#     print(solution(n, info))
# Countdown (Google Kickstart 2020 Round C)
# 
# Url: https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2
#
#   
# Hint
# 1. 코드가 상태머신의 형태로 정의되는 경우가 있다
# 2. 상태머신의 상태를 표현하는 메모리를 만들어 코드를 작성할 수 있다
# 
#
# 풀이
# - 유한상태머신(Finite State Machine, FSM)은 유한한 상태를 순회하며 특정한 작업을
#   수행하는 머신을 말한다. 보통 FSM은 물리적인 머신을 말하지만, 알고리즘 또한 이러한
#   형태로 작성될 수 있다.
# 
# - 이 문제의 경우 알고리즘이 크게 두 가지의 상태를 순회한다.
# 
# - 상태: 
#   S0: 현재 카운트다운이 감지되지 않음 (대기 상태)
#   S1: 카운트다운이 감지됨
# 
# - 상태머신은 숫자를 차례대로 순회하며 카운트다운을 감지한다. 이때, 초기상태는
#   S0이다. 현재 숫자가 카운트다운의 시작지점이 될 수 있다면 상태머신은 S1으로
#   바뀐다. S1으로 바뀐 후 그대로 카운트다운이 유지되는지를 확인한다. 만약 S1인
#   상태로 카운트다운이 유지되어 1에 도달하였으면 최종적으로 하나의 카운트다운을
#   감지하였으므로 감지한 카운트다운의 개수를 1 증가시킨 후 S0으로 이동한다. 만약
#   S1인 상태에서 다음 숫자가 카운트다운의 일부분이 아니라면 곧바로 S0으로 이동한다.
# 
# - 현재 가능한 상태가 2개 이므로 1비트의 메모리만으로 상태를 표현할 수 있다. 아래
#   코드에서는 flag라는 변수가 이에 해당한다. ('flag'는 알고리즘의 분기를 물리적으로
#   표현하는데 많이 사용되는 변수명이다)
# 
# - 만약 상태의 개수가 2개 보다 많다면 필요한 메모리의 공간도 많아지게 된다. 


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N, K = map(int, input().split())
        seq = list(map(int, input().split()))

        # S0: flag가 false, S1: flag가 true
        # 초기상태는 S0이다
        flag, cnt = False, 0

        for idx, num in enumerate(seq):
            if num == K:
                # 카운트다운의 시작지점을 감지 -> S1으로 전환
                # 현재 상태는 S0이다
                flag = True
            elif flag:
                # 현재 상태가 S1인 경우
                if seq[idx] == seq[idx-1] - 1:
                    # 만약 카운트다운이 유지되는 경우
                    if num == 1:
                        # 1을 만난 경우 -> cnt증가, S0으로 전환
                        cnt += 1
                        flag = False
                    # 1을 만나지 않았으면 현재 상태 유지
                else:
                    # 카운트다운이 유지되지 않았다면 -> S0으로 전환
                    flag = False

        print("Case #{}: {}".format(t, cnt))
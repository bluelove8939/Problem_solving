from sys import stdin


def search_bin(st, ed, pset, skill):
    st_idx = -1
    left, right = 0, len(problems) - 1

    while right >= left:
        center = int((right + left) / 2)

        if st[center] <= skill:
            st_idx = center
            left = center + 1
        else:
            right = center - 1
            
    ed_idx = -1
    left, right = 0, len(problems) - 1

    while right >= left:
        center = int((right + left) / 2)

        if ed[center] >= skill:
            ed_idx = center
            right = center - 1
        else:
            left = center + 1
    
    return st_idx, ed_idx
            
            
if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        N, M = map(int, stdin.readline().split())
        problems = [list(map(int, stdin.readline().split())) for _ in range(N)]
        students = list(map(int, stdin.readline().split()))

        st = sorted([prob[0] for prob in problems])
        ed = sorted([prob[1] for prob in problems])
        pset = []

        for skill in students:
            st_idx = 0
            ed_idx = -1
            diff = 0

            while True:
                st_idx, ed_idx = search_bin(st, ed, pset, skill - diff)
                
                if st_idx == ed_idx:
                    if (skill - diff) not in pset:
                        pset.append(skill - diff)
                        break
                    else:
                        flag = False

                        for diff in range(diff, max(skill - st[st_idx], ed[st_idx] - skill)):
                            if (skill - diff) >= st[st_idx] and (skill - diff) not in pset:
                                flag = True
                                pset.append(skill-diff)
                                break

                            if (skill - diff) <= ed[ed_idx] and (skill + diff) not in pset:
                                flag = True
                                pset.append(skill+diff)
                                break

                        if flag:
                            break

                        diff += 1
                else:
                    if st_idx == -1 or ed_idx == -1:
                        diff = skill - ed[-1]
                    else:
                        diff = skill - ed[st_idx]


        print(f"Case #{t}: {' '.join(map(str, pset))}")
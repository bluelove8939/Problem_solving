from sys import stdin


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        N, C = map(int, input().split())
        intervals = [list(map(int, stdin.readline().split())) for _ in range(N)]

        st = sorted([item[0] for item in intervals])
        ed = sorted([item[1] for item in intervals])
        
        left, right = 0, 0
        cur, pri = 0, 0
        cnt = 0
        res = []

        while True:
            new_cnt = cnt

            if left < len(st) and cur == st[left]:
                while left < len(st) and st[left] <= cur:
                    left += 1
                    new_cnt += 1
            
            if right < len(ed) and cur == ed[right]:
                while right < len(ed) and ed[right] <= cur:
                    right += 1
                    cnt -= 1
                    new_cnt -= 1
            
            res.append(cnt)

            

            cnt = new_cnt

        res.sort(reverse=True)

        print(f"Case #{t}: {len(intervals) + sum(res[0:C])}")

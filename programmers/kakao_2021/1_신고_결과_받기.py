def solution(id_list, report, k):
    rpt_dict = dict()

    for id_name in id_list:
        rpt_dict[id_name] = [0, [], 0]

    for ln in report:
        rpt_id, vic_id = ln.split()
        if rpt_id not in rpt_dict[vic_id][1]:
            rpt_dict[vic_id][0] += 1
            rpt_dict[vic_id][1].append(rpt_id)

    for vic_name in id_list:
        if rpt_dict[vic_name][0] >=k:
            for rpt_id in rpt_dict[vic_name][1]:
                rpt_dict[rpt_id][2] += 1

    answer = [rpt_dict[id_name][2] for id_name in id_list]
    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    print(solution(id_list, report, k))
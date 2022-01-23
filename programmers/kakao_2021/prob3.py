def solution(fees, records):
    free_time, basic_fee, unit_time, unit_fee = fees
    calc_fees = dict()

    for rec in records:
        timestamp, carnum, inout = rec.split()
        hours, mins = map(int, timestamp.split(':'))
        carnum = int(carnum)

        if inout == "IN":
            if carnum not in calc_fees.keys():
                calc_fees[carnum] = [hours, mins, 0, -1]
            else:
                calc_fees[carnum][0] = hours
                calc_fees[carnum][1] = mins
        else:
            time_diff = (hours - calc_fees[carnum][0]) * 60 + (mins - calc_fees[carnum][1])
            calc_fees[carnum][2] += time_diff
            calc_fees[carnum][0] = -1

    for carnum in calc_fees.keys():
        if calc_fees[carnum][0] != -1:
            time_diff = (23 - calc_fees[carnum][0]) * 60 + (59 - calc_fees[carnum][1])
            calc_fees[carnum][2] += time_diff
        time_diff = calc_fees[carnum][2] - free_time
        if time_diff < 0: time_diff = 0
        calc_fees[carnum][3] = basic_fee + (time_diff // unit_time + (1 if time_diff % unit_time != 0 else 0)) * unit_fee

    answer = [calc_fees[carnum][3] for carnum in sorted(calc_fees.keys())]
    return answer


# if __name__ == '__main__':
#     fees = [180, 5000, 10, 600]
#     records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#
#     print(solution(fees, records))
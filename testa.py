def solution(periods, payments, estimates):

    answer = [0 for i in range(2)]

    for i in range(len(periods)):
        curr_sum = 0
        next_mon_sum = 0
        for j in range(12):
            curr_sum += payments[i][j]
            if j != 0:
                next_mon_sum += payments[i][j]

        if periods[i] >= 24 and periods[i] < 59:
            if curr_sum >= 900000:
                if next_mon_sum + estimates[i] < 900000:
                    answer[1] += 1
            elif curr_sum < 900000:
                if next_mon_sum + estimates[i] >= 900000:
                    answer[0] += 1
        elif periods[i] == 23:
            if next_mon_sum + estimates[i] >= 900000:
                answer[0] += 1
        elif periods[i] >= 60:
            if curr_sum >= 600000:
                if next_mon_sum + estimates[i] < 600000:
                    answer[1] += 1
            elif curr_sum < 600000:
                if next_mon_sum + estimates[i] >= 600000:
                    answer[0] += 1
        elif periods[i] == 59:
            if curr_sum >= 900000:
                if next_mon_sum + estimates[i] < 600000:
                    answer[1] += 1
            if curr_sum < 900000:
                if next_mon_sum + estimates[i] >= 600000:
                    answer[0] += 1

    return answer

print(solution([24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [350000, 50000, 40000, 50000]))
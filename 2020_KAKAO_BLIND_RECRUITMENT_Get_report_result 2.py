def solution(id_list, report, k):
    user = {}
    user_report_index = {}
    report_count = {}
    answer = []
    
    for i in range(len(id_list)):
        user[id_list[i]] = []
        user_report_index[id_list[i]]= {}
        report_count[id_list[i]] = 0
        answer.append(0)

    for i in range(len(report)):
        tmp = report[i].split()
        try:
            if user_report_index[tmp[0]][tmp[1]] == None:
                report_count[tmp[1]] += 1
        except:
            user_report_index[tmp[0]][tmp[1]] = len(user[tmp[0]])
            user[tmp[0]].append(tmp[1])
            report_count[tmp[1]] += 1

    for i in range(len(id_list)):
        for j in range(len(user[id_list[i]])):
            if report_count[user[id_list[i]][j]] >= k:
                answer[i] += 1

    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
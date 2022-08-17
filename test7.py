def solution(n, lost, reserve):
    answer = n - len(lost)

    tmp = [0 for i in range(n)]
    for i in range(len(reserve)):
        tmp[reserve[i]] = 1

    for i in range(len(lost)):
        if lost[i] != 1 and lost[i] != n:
            if tmp[lost[i] - 1] == 1 and tmp[lost[i] + 1] == 1:
                continue
            else:
                answer += 1
                del lost[i]
        elif lost[i] != 1:
             if tmp[lost[i] + 1] == 1:
                answer += 1
                del lost[i]
        elif lost[i] == n:
            if tmp[lost[i] - 1] == 1:
                answer += 1
                del lost[i]

        if i + 1 >= len(lost):
            break

    for i in range(len(lost)):
        if lost[i] != 1 and lost[i] != n:
            answer += 1
            del lost[i]

        if i + 1 >= len(lost):
            break

    return answer

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))
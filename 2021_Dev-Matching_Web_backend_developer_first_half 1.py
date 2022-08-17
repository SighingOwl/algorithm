def solution(lottos, win_nums):
    answer = []
    
    non_zero = []
    for i in range(len(lottos)):
        if lottos[i] != 0:
            non_zero.append(lottos[i])
    
    min_matched = 0
    for i in range(len(non_zero)):
        try:
            win_nums.index(non_zero[i])
            min_matched += 1
        except ValueError:
            continue
    
    max_matched = min_matched + len(lottos) - len(non_zero)
    
    if max_matched == 6:
        answer.append(1)
    elif max_matched == 5:
        answer.append(2)
    elif max_matched == 4:
        answer.append(3)
    elif max_matched == 3:
        answer.append(4)
    elif max_matched == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if min_matched == 6:
        answer.append(1)
    elif min_matched == 5:
        answer.append(2)
    elif min_matched == 4:
        answer.append(3)
    elif min_matched == 3:
        answer.append(4)
    elif min_matched == 2:
        answer.append(5)
    else:
        answer.append(6)

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
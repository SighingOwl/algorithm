import re

def solution(dartResult):
    num = re.split('[|S|T|D|*|#]', dartResult)
    for i in range(len(num)):
        if num[i] == '':
            del num[i]
        if i >= len(num):
            break
            
    num_index = 0
    answer = 0
    tmp = 0
    
    for i in range(len(dartResult)):
        if dartResult[i] == "S":
            if i + 1 < len(dartResult) and dartResult[i + 1] == "#":
                answer -= int(num[num_index]) ** 1
                num_index += 1
            else:
                answer += int(num[num_index]) ** 1
                num_index += 1
            
        elif dartResult[i] == "D":
            if i + 1 < len(dartResult) and dartResult[i + 1] == "#":
                answer -= int(num[num_index]) ** 2
                num_index += 1
            else:
                answer += int(num[num_index]) ** 2
                num_index += 1
        elif dartResult[i] == "T":
            if i + 1 < len(dartResult) and dartResult[i + 1] == "#":
                answer -= int(num[num_index]) ** 3
                num_index += 1
            else:
                answer += int(num[num_index]) ** 3
                num_index += 1
        elif dartResult[i] == "*":
            answer *= 2
        elif dartResult[i] == "#":
            continue

    return answer
'''
for i in range(10):
    print(solution(input()))
    '''
print(solution(input()))
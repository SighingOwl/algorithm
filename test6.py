def listToString(str_list):
    result = ""
    for s in str_list:
        result += s
    return result.strip()

def solution(s):
    tmp = []
    for i in range(len(s)):
        tmp.append(s[i])

    tmp.sort(reverse = True)

    answer = listToString(tmp)

    return answer

print(solution(input()))
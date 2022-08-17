def listToString(A):
    result = ""
    for s in A:
        result += s
    return result.strip()

def solution(s):
    index = 0
    tmp_str = []
    for i in range(len(s)):
        if s[i] != " ":
            if index % 2 == 0:
                tmp = s[i]
                tmp = tmp.upper()
                tmp_str.append(tmp)
                tmp = []
                index += 1
            else:
                tmp_str.append(s[i])
                index += 1
        else:
            tmp_str.append(s[i])
            index = 0

    answer = listToString(tmp_str)

    return answer

print(solution(input()))
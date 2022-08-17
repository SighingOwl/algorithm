def listToString(str_list):
    result = ''
    for s in str_list:
        result += s
    return result.strip()

def solution(new_id):
    new_id = new_id.lower()
    tmp = []
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == "-" or new_id[i] == "_" or new_id[i] == ".":
            tmp.append(new_id[i])
    
    for i in range(len(tmp) - 1):
        while True:
            if i + 1 < len(tmp) - 1 and tmp[i] == "." and tmp[i + 1] == ".":
                del tmp[i + 1]
            else:
                break
    
    tmp_id = listToString(tmp)
    
    tmp_id = tmp_id.lstrip(".")
    tmp_id = tmp_id.rstrip(".")
    
    if not tmp_id:
        tmp_id += "a"
    
    if len(tmp_id) >= 16:
        tmp_id = tmp_id[0:15]
        tmp_id = tmp_id.lstrip(".")
        tmp_id = tmp_id.rstrip(".")
    
    while len(tmp_id) <= 2:
        tmp_id += tmp_id[-1]
    
    answer = tmp_id
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))
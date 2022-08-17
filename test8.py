import re

def info_parsing(info):
    info2 = [[] for i in range(5)]
    for i in range(len(info)):
        tmp = info[i].split()
        for j in range(5):
            info2[i].append(tmp[j])
            
    info.sort(key = lambda x : (x[0], x[1], x[2], x[3], x[4])
    
    return info2

def query_parsing(query):
    query2 = [[] for i in raneg(5)]
    for i in range(len(query)):
        tmp = query[i].split()
        for j in range(len(tmp)):
            if tmp[j] != "and":
                query2[i].append(tmp[j])
                
    return query2

def indexing_info(info):
    info_index = [[[[[] for l in range(2)] for k in range(2)] for j in range(2)] for i in range(3)]
    for i in range(len(query_parsed)):
        if info[0] == "cpp":
            if info[1] == "backend":
                if info[2] == "junior":
                    if info[3] == "chicken":
                        info_index[0][0][0][0].append(info[4])
                    else:
                        info_index[0][0][0][1].append(info[4])
                else:
                    if info[3] == "chicken":
                        info_index[0][0][1][0].append(info[4])
                    else:
                        info_index[0][0][1][1].append(info[4])
            else:
                if info[2] == "junior":
                    if info[3] == "chicken":
                        info_index[0][1][0][0].append(info[4])
                    else:
                        info_index[0][1][0][1].append(info[4])
                else:
                    if info[3] == "chicken":
                        info_index[0][1][1][0].append(info[4])
                    else:
                        info_index[0][1][1][1].append(info[4])
        elif info[1] == "java":
            if info[1] == "backend":
                if info[2] == "junior":
                    if info[3] == "chicken":
                        info_index[1][0][0][0].append(info[4])
                    else:
                        info_index[1][0][0][1].append(info[4])
                else:
                    if info[3] == "chicken":
                        info_index[1][0][1][0].append(info[4])
                    else:
                        info_index[1][0][1][1].append(info[4])
            else:
                if info[2] == "junior":
                    if info[3] == "chicken":
                        info_index[1][1][0][0].append(info[4])
                    else:
                        info_index[1][1][0][1].append(info[4])
                else:
                    if info[3] == "chicken":
                        info_index[1][1][1][0].append(info[4])
                    else:
                        info_index[1][1][1][1].append(info[4])
        else:
            if info[1] == "backend":
                if info[2] == "junior":
                    if info[3] == "chicken":
                        info_index[3][0][0][0].append(info[4])
                    else:
                        info_index[3][0][0][1].append(info[4])
                else:
                    if info[3] == "chicken":
                        info_index[3][0][1][0].append(info[4])
                    else:
                        info_index[3][0][1][1].append(info[4])
            else:
              if info[2] == "junior":
                    if info[3] == "chicken":
                        info_index[3][1][0][0].append(info[4])
                    else:
                        info[3][1][0][1].append(info[4])
                else:
                    if info[3] == "chicken":
                        info_index[3][1][1][0].append(info[4])
                    else:
                        info_index[3][1][1][1].append(info[4])
    
    return info_index

def process_query(query_parsed, info):
    count = 0
    if query_parsed[0] == "cpp":
        if query_parsed[1] == "backend":
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[0][0][0][0]):
                        if info[0][0][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[0][0][0][1]):
                        if info[0][0][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[0][0][1][0]):
                        if info[0][0][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[0][0][1][1]):
                        if info[0][0][1][1][i] >= query_parsed[i]
                            count += 1
        else:
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[0][1][0][0]):
                        if info[0][1][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[0][1][0][1]):
                        if info[0][1][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[0][1][1][0]):
                        if info[0][1][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[0][1][1][1]):
                        if info[0][1][1][1][i] >= query_parsed[i]
                            count += 1
    elif query_parsed[0] == "java":
        if query_parsed[1] == "backend":
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[1][0][0][0]):
                        if info[1][0][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[1][0][0][1]):
                        if info[1][0][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[1][0][1][0]):
                        if info[1][0][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[1][0][1][1]):
                        if info[1][0][1][1][i] >= query_parsed[i]
                            count += 1
        else:
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[1][1][0][0]):
                        if info[1][1][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[1][1][0][1]):
                        if info[1][1][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[1][1][1][0]):
                        if info[1][1][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[1][1][1][1]):
                        if info[1][1][1][1][i] >= query_parsed[i]
                            count += 1
    elif query_parsed[0] == "python":
        if query_parsed[1] == "backend":
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[2][0][0][0]):
                        if info[2][0][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][0][0][1]):
                        if info[2][0][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[2][0][1][0]):
                        if info[2][0][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][0][1][1]):
                        if info[2][0][1][1][i] >= query_parsed[i]
                            count += 1
        else:
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[2][1][0][0]):
                        if info[2][1][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][1][0][1]):
                        if info[2][1][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[2][1][1][0]):
                        if info[2][1][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][1][1][1]):
                        if info[2][1][1][1][i] >= query_parsed[i]
                            count += 1
    else:
        if query_parsed[1] == "backend":
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[2][0][0][0]):
                        if info[2][0][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][0][0][1]):
                        if info[2][0][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[2][0][1][0]):
                        if info[2][0][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][0][1][1]):
                        if info[2][0][1][1][i] >= query_parsed[i]
                            count += 1
        elif query_parsed[1] == "frontend":
            if query_parsed[2] == "junior":
                if query_parsed[3] == "chicken":
                    for i in range(info[2][1][0][0]):
                        if info[2][1][0][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][1][0][1]):
                        if info[2][1][0][1][i] >= query_parsed[i]
                            count += 1
            else:
                if query_parsed[3] == "chicken":
                    for i in range(info[2][1][1][0]):
                        if info[2][1][1][0][i] >= query_parsed[i]
                            count += 1
                else:
                    for i in range(info[2][1][1][1]):
                        if info[2][1][1][1][i] >= query_parsed[i]
                            count += 1
        else:
              
def solution(info, query):
    
    info_parsed = info_parsing(info)
    query_parsed = query_parsing(query)
    indexed_info = indexing_info(info_parsed)

    answer = []
    for i in range(len(query_parsed))
        result = process_query(query_parsed[i])
        answer.append(result)

    return answer
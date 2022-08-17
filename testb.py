def solution(n, plans, clients):
    answer = [0 for i in range(len(clients))]

    plans_charge = []
    plans_service = [[] for i in range(len(plans))]
    for i in range(len(plans)):
        plans[i] = plans[i].split()
        plans_charge.append(int(plans[i][0]))
        if i != 0:
            for j in range(len(plans_service[i - 1])):
                plans_service[i].append(plans_service[i - 1][j])

            for j in range(1, len(plans[i])):
                plans_service[i].append(int(plans[i][j]))
        else:
            for j in range(1, len(plans[i])):
                plans_service[i].append(int(plans[i][j]))
    
    for i in range(len(clients)):
        clients[i] = clients[i].split()
        for j in range(len(clients[i])):
            clients[i][j] = int(clients[i][j])

    for i in range(len(clients)):
        for j in range(len(plans)):
            if clients[i][0] <= plans_charge[j]:
                can_provide = []
                for k in range(1, len(clients[i])):
                    try:
                        can_provide.append(plans_service[j].index(clients[i][k]))
                    except:
                        continue
                if len(can_provide) >= len(clients[i]) - 1:
                    answer[i] = j + 1
                    break

    return answer


print(solution(3, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
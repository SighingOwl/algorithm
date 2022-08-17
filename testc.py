def solution(grid, k):
    answer = -1

    camp_site = find_camp_site(grid, [0, 0], k)
    print(camp_site)


    return answer

def find_camp_site(grid, curr_loc, k):
    if k == 0:
        if grid[curr_loc[0]][curr_loc[1]] == '.':
            return [curr_loc]
        else:
            return [None]
    
    up_result = []
    right_result = []
    down_result = []
    left_result = []

    if curr_loc[0] != 0:
        next_loc = []
        next_loc.append(curr_loc[0] - 1)
        next_loc.append(curr_loc[1])

        if grid[next_loc[0]][next_loc[1]] != '#':
            up_result = find_camp_site(grid, next_loc, k - 1)
        elif grid[next_loc[0]][next_loc[1]] == "." and k != 1:
            up_result.append(next_loc)
        else:
            up_result = [None]

    if curr_loc[1] != len(grid[0]) - 1:
        next_loc = []
        next_loc.append(curr_loc[0])
        next_loc.append(curr_loc[1] + 1)

        if grid[next_loc[0]][next_loc[1]] != '#':
            right_result = find_camp_site(grid, next_loc, k - 1)
        elif grid[next_loc[0]][next_loc[1]] == "." and k != 1:
            right_result.append(next_loc)
        else:
            right_result = [None]

    if curr_loc[0] != len(grid) - 1:
        next_loc = []
        next_loc.append(curr_loc[0] + 1)
        next_loc.append(curr_loc[1])

        if grid[next_loc[0]][next_loc[1]] != '#':
            down_result  = find_camp_site(grid, next_loc, k - 1)
        elif grid[next_loc[0]][next_loc[1]] == "." and k != 1:
            down_result.append(next_loc)
        else:
            down_result = [None]

    if curr_loc[1] != 0:
        next_loc = []
        next_loc.append(curr_loc[0])
        next_loc.append(curr_loc[1] - 1)

        if grid[next_loc[0]][next_loc[1]] != '#':
            left_result = find_camp_site(grid, next_loc, k - 1)
        elif grid[next_loc[0]][next_loc[1]] == "." and k != 1:
            left_result.append(next_loc)
        else:
            left_result = [None]

    result = []
    for i in range(len(up_result)):
        if up_result[i] != None:
            try:
                result.index(up_result[i])
            except:
                result.append(up_result[i])
    
    for i in range(len(right_result)):
        if right_result[i] != None:
            try:
                result.index(right_result[i])
            except:
                result.append(right_result[i])

    for i in range(len(down_result)):
        if down_result[i] != None:
            try:
                result.index(down_result[i])
            except:
                result.append(down_result[i])

    for i in range(len(left_result)):
        if left_result[i] != None:
            try:
                result.index(left_result[i])
            except:
                result.append(left_result[i])

    return result


print(solution(["..FF", "###F", "###."], 4))
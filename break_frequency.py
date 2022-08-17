n = int(input())
frequency = []
for i in range(n):
    frequency.append([int(x) for x in input().split()])

frequency_dict = {}
for i in range(n):
    for j in range(1, len(frequency[i])):
        try:
            frequency_dict[frequency[i][j]][0] += 1
            frequency_dict[frequency[i][j]].append(i)
        except:
            frequency_dict[frequency[i][j]] = [1, i]

frequency_dict = sorted(frequency_dict.items(), key = lambda item: item[1], reverse=True)

town = {}
for i in range(n):
    town[i] = 1

#print(town)
#print(frequency_dict)
#print(type(frequency_dict[0][1]))
on_count = n
target_count = n
frequency_count = 0
for i in range(len(frequency_dict)):
    for j in range(1, len(frequency_dict[i][1])):
        if town[frequency_dict[i][1][j]] == 1:
            on_count -= 1
            town[frequency_dict[i][1][j]] = 0
    
    if on_count == 0:
        frequency_count += 1
        break
    elif on_count != 0:
        if on_count != target_count:
            frequency_count += 1
        target_count = on_count
        
print(frequency_count)
        
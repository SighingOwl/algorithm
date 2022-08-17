# 3의 배수 처리 해야한다.

def solution(n):
    
    ternary = []
    
    while n != 0:
        if n % 3 == 0:
            ternary.append(n % 3)
            n = n // 3 - 1
        else:
            ternary.append(n % 3)
            n = n // 3
        
    answer = 0    
    for i in range(len(ternary) - 1, -1, -1):
        if ternary[i] == 1:
            answer = answer * 10 + 1
        elif ternary[i] == 2:
            answer = answer * 10 + 2
        elif ternary[i] == 0:
            answer = answer * 10 + 4
    
    return str(answer)

print(solution(3))
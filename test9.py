def solution(s):
    answer = -1
    
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0 or stack[-1] != s[i]:
            stack.append(s[i])
        
        elif stack[-1] == s[i]:
            stack.pop()
                
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer
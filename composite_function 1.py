"""
*해결방법
    - "f_dict" dict에 1, 2, ... , n까지 정수를 key로 하는 value에 n개의 f(x)값을 순서대로 저장하고 이를 "getValue"에서 query로 들어온 x와 x를 인자로 하는 f(x)의 합성 횟수를 사용해서 결과를 출력했다.
    - "getValue"함수는 아래와 같이 동작한다.
        1. 함수가 시작되면 가장 먼저 x = query[0], 합성 횟수를 뜻하는 "compose_count"변수에는 query[1]를 저장한다.
        2. compose_count만큼 for loop를 실행하며 f(x)의 결과에 result가 되며 다음 차례의 x를 result로 설정한다.
        3. 위 두 과정을 반복하여 합성 함수의 결과를 도출한다. 

*시간 복잡도
    - "f_dict"에 함수값을 저장하는데 O(n)의 시간 복잡도가 필요하다.
    - "getValue"에서 합성 함수의 결과를 도출할 때까지 query에 들어온 합성 횟수만큼의 반복이 필요하므로 합성 횟수를 c라고 할 때 O(c)의 시간 복잡도가 필요하다. c의 범위는 0 이상이라 추측되며 문제에서 범위를 정해놓지 않아 최악의 경우를 n이라 할 수 없다. 제시된 합성 함수가 전단사 함수가 아닌 경우 n번보다 더 많이 반복할 수 있기 때문이다.
    - "getValue"함수를 q번 호출하므로 전체 query를 처리할 때까지 O(cq)의 시간 복잡도가 필요하다.
    - 전체 알고리즘의 시간 복잡도는 O(cq)이다.
"""

def getValue(query, f):
    x = query[0]
    compose_count = query[1]
    result = 0

    for i in range(compose_count):
        result = f[x]
        x = result
    
    print(result)

n = int(input())

f_dict = {}
i = 1
for x in input().split():
    f_dict[i] = int(x)
    i += 1

q = int(input())
query = []
for i in range(q):
    getValue([int(x) for x in input().split()], f_dict)

print(n, q)
print(query)
print(f_dict)
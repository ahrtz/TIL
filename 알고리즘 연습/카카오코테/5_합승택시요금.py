# def solution(n, s, a, b, fares):


n=6
s=	4
a=	6
b=	2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

INF = int(1e9)                                  #무한을 의미하는 값 10억 설정
graph = [[INF] * n for _ in range(n)]			

for i in range(n):                              #자기 자신으로 가는 비용 0
    graph[i][i] = 0

for i in fares:
    graph[i[0] - 1][i[1] - 1] = i[2]            #이동 방향에 따라 비용이 달라지지 않으므로
    graph[i[1] - 1][i[0] - 1] = i[2]			

for t in range(n):
    for i in range(n):
        for j in range(i, n):                   
            if i != j:                          #최소 비용 계산
                temp = min(graph[i][j], graph[i][t] + graph[t][j]) 
                graph[i][j] = graph[j][i] = temp
print(graph)
answer = INF
for t in range(n):                              #경유점에 따라 최소 합승 비용 탐색
    temp = graph[s - 1][t] + graph[t][b - 1] + graph[t][a - 1]      
    answer = min(answer, temp)

print(answer)    # return answer
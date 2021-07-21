import sys
input=sys.stdin.readline

N,M=map(int,input().split())

# 인접리스트
graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)

def dfs(v):
    visited[v]=True
    for j in graph[v]:
        if not visited[j]:
            dfs(j)
cnt=0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)
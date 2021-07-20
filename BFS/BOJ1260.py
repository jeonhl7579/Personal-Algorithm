import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())
arr=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    arr[a][b]=arr[b][a]=1

visit=[0]*(N+1)

def bfs(v):
    q=[]
    q.append(v)
    visit[v]=1

    while q:
        a=q.pop(0)
        print(a,end=" ")
        for i in range(1,N+1):
            if visit[i]==0 and arr[a][i] == 1:
                q.append(i)
                visit[i]=1

bfs(V)
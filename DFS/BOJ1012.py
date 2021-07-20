import sys
input=sys.stdin.readline

Testcase=int(input())

def dfs(farm,M,N,x,y):
    if 0<=x and x<M and 0<=y and y<N:
        if farm[y][x]==1:
            farm[y][x]=0

            dfs(farm,M,N,y+1,x)
            dfs(farm,M,N,y-1,x)
            dfs(farm,M,N,y,x+1)
            dfs(farm,M,N,y,x-1)

for _ in range(Testcase):
    M,N,K=map(int,input().split())
    farm=[[0]*M for _ in range(N)]
    cnt=0
    for i in range(K):
        a,b=map(int,input().split())
        farm[b][a]=1
    print(farm)
    for i in range(M):
        for j in range(N):
            if farm[j][i]==1:
                print([j,i])
                dfs(farm,M,N,i,j)
                cnt+=1

    print(cnt)
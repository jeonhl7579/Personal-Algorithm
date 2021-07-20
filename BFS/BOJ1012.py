import sys
from collections import deque
input=sys.stdin.readline

Testcase=int(input())

def bfs(farm,M,N,x,y):
    q=deque()
    q.append((x,y))

    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    farm[x][y]=1
    cnt=0

    while q:
        a,b=q.popleft()
        
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]

            if 0<=na and na<N and 0<=nb and nb<M:
                if farm[na][nb] == 1:
                    farm[na][nb]=0
                    q.append((na,nb))
                    cnt+=1

    return cnt 

for _ in range(Testcase):
    M,N,K=map(int,input().split())
    farm=[[0]*M for _ in range(N)]
    result=[]
    for i in range(K):
        a,b=map(int,input().split())
        farm[b][a]=1
    print(farm)
    for i in range(M):
        for j in range(N):
            if farm[j][i]==1:
                print([j,i])
                result.append(bfs(farm,M,N,j,i))
                

    print(len(result))
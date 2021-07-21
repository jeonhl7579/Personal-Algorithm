import sys
from collections import deque
input=sys.stdin.readline

M,N,K=map(int,input().split())
area=[[0]*N for _ in range(M)]

for _ in range(K):
    lx,ly,rx,ry=map(int,input().split())
    for i in range(lx,rx):
        for j in range(ly,ry):
            area[j][i]=1

def bfs(x,y):
    result=0
    q=deque()
    q.append((x,y))
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]

    while q:
        a,b=q.popleft()
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            if 0<=na and na<M and 0<=nb and nb<N:
                if area[na][nb]==0:
                    result+=1
                    area[na][nb]=1
                    q.append((na,nb))
    
    return result

value=[]
for i in range(M):
    for j in range(N):
        if area[i][j]==0:
            a=bfs(i,j)
            if a==0:
                value.append(1)
            else:
                value.append(a)

print(len(value))
for i in sorted(value):
    print(i,end=' ')
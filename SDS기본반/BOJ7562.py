import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

def bfs(sx,sy,lx,ly):
    q=deque()
    q.append((sx,sy))
    chess[sx][sy]=1
    dy=[2,1,-1,-2,-2,-1,1,2]
    dx=[1,2,2,1,-1,-2,-2,-1]

    while q:
        a,b=q.popleft()
        if a==lx and b==ly:
            break
        
        for i in range(8):
            na=a+dx[i]
            nb=b+dy[i]
            if 0<=na and na<l and 0<=nb and nb<l and chess[na][nb]==0:
                chess[na][nb]=chess[a][b]+1
                q.append((na,nb))

for _ in range(t):
    l=int(input())
    chess=[[0]*l for _ in range(l)]
    sx,sy=map(int,input().split())
    lx,ly=map(int,input().split())
    bfs(sx,sy,lx,ly)
    print(chess[lx][ly]-1)
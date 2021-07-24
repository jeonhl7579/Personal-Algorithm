import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
miro=[]
for i in range(N):
    miro.append(list(map(int,input().rstrip())))

#print(miro)
def bfs(x,y):
    q=deque()
    q.append((x,y))

    dx=[-1,1,0,0]
    dy=[0,0,1,-1]

    while q:
        a,b=q.popleft()

        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]

            if 0<=na and na<N and 0<=nb and nb<M:
                if miro[na][nb] == 1:
                    miro[na][nb]=miro[na][nb]+miro[a][b]
                    q.append((na,nb))
for i in range(N):
    for j in range(M):
        if miro[i][j]==1:
            bfs(i,j)
print(miro[N-1][M-1])
#print(miro)

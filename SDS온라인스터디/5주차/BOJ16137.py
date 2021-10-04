import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
crow_map=[]
for _ in range(n):
    crow_map.append(list(map(int,input().split())))

visit=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if crow_map[i][j]==1:
            visit[i][j]=True
        if crow_map[i][j] >=2:
            cy=crow_map[i][j]
            px,py=i,j

# n은 맵의 크기, m은 오작교 생성하는 주기
# 맵에서 2보다 큰 값은 해당 주기마다 추가로 생성되는 오작교
# 마무리하기
# 2보다 큰 주기로 생성되는 오작교만 따로
def make_bridge(y,x,n,m,crow_map,visit):
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    q=deque()
    q.append([y,x])
    visit[y][x]=False
    cycle=0
    while q:
        if cycle==cy:
            visit[px][py]=True
            cycle=0
        else:
            if visit[px][py]:
                visit[px][py]=False

        a,b=q.popleft()
        if a==n-1 and b==n-1:
            break
        # 주기가 되었으면
        if (crow_map[a][b]%m)==0:
            for i in range(4):
                na=a+dy[i]
                nb=b+dx[i]
                if 0>na or 0>nb or na>=n or nb>=n:
                    continue
                if crow_map[na][nb]==0:
                    visit[na][nb]=True
                    crow_map[na][nb]=1

        for i in range(4):
            na=a+dy[i]
            nb=b+dx[i]

            if 0>na or 0>nb or na>=n or nb>=n or visit[na][nb]==False:
                continue
            elif visit[na][nb]==True:
                crow_map[na][nb]+=crow_map[a][b]
                q.append([na,nb])
                visit[na][nb]=False
        cycle+=1

make_bridge(0,0,n,m,crow_map,visit)

print(crow_map[n-1][n-1]-1)
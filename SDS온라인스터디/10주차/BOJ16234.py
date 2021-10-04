# 문제 : 인구 이동
# 내용 : n*n 인 2차 배열에서 인구 이동이 일어난다.
#        두 나라의 인구 차이가 L명 이상 R명 이하이면 국경선을 연다.
#        탐색 후에 국경선 여는 과정이 끝났으면 인구 이동을 시작
#        인접한 두 나라의 인구 차이를 구한 후 L이상 R이하인지 확인
import sys
from collections import deque, namedtuple
input=sys.stdin.readline


def bfs(i,j):
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    q=deque()
    q.append([i,j])
    tmp=[]
    tmp.append([i,j])

    while q:
        a,b=q.popleft()
        for i in range(4):
            na=a+dy[i]
            nb=b+dx[i]

            if 0<=na<n and 0<=nb<n and visit[na][nb]==0:
                if l<=abs(arr[na][nb]-arr[a][b])<=r:
                    visit[na][nb]=1
                    q.append([na,nb])
                    tmp.append([na,nb])
    return tmp
    
n,l,r=map(int,input().split())
arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))
cnt=0
while True:
    visit=[[0]*n for _ in range(n)]
    isTrue=False
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                visit[i][j]=1
                tmp=bfs(i,j)
                if len(tmp)>1:
                    isTrue=True
                    num=sum([arr[x][y] for x,y in tmp])//len(tmp)
                    for x,y in tmp:
                        arr[x][y]=num
    if not isTrue:
        break
    cnt+=1

print(cnt)



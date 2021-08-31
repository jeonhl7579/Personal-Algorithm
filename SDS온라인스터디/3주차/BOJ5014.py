import sys
from collections import deque
input=sys.stdin.readline

f,s,g,u,d=map(int,input().split())
elevator=[-1]*(f+1)
# 건물의 층수는 f
# 스타트링크의 위치는 g
# 강호의 위치는 s
# u는 위로 u 증가
# d는 아래로 d 감소
# f=10, s=1, g=10, u=2,d=1

direction=[u,(-d)]
def bfs(num):
    queue=deque()
    queue.append(num)
    visit=[False for _ in range(f+1)]
    visit[num]=True

    while queue:
        a=queue.popleft()
        for i in range(2):
            na=a+direction[i]
            if na>0 and na<=f and visit[na]==False:
                visit[na]=True
                queue.append(na)
                elevator[na]=elevator[a]+1
    #print(visit)

elevator[s]=0
bfs(s)

if elevator[g]==-1:
    print('use the stairs')
else:
    print(elevator[g])
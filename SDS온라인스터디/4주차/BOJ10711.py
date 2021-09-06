import sys
from collections import deque
input=sys.stdin.readline

h,w=map(int,input().split())
sand=[]

def bfs(sand,y,x,num):
    global h,w
    # 8방향
    dy=[-1,-1,0,1,1,1,0,-1]
    dx=[0,1,1,1,0,-1,-1,-1]
    q=deque()
    q.append([y,x])
    cnt=0
    while q:
        a,b=q.popleft()
        for i in range(8):
            ny=y+dy[i]
            nx=x+dx[i]

            if 0>ny or 0>nx or ny>=h or nx>=w:
                continue
            if sand[ny][nx]=='.':
                cnt+=1
    if cnt>=num:
        return True

for _ in range(h):
    sand.append(list(input().strip()))

flag=False
round=0
arr=[]
while not flag:
    for i in range(h):
        for j in range(w):
            if sand[i][j]=='.':
                continue
            else:
                # True이면 휩쓸리는 모래성
                b=bfs(sand,i,j,int(sand[i][j]))
                if b:
                    #print(i,j)
                    arr.append([i,j])
    #print(arr)
    if len(arr)==0:
        flag=True
    elif len(arr)>0:
        while arr:
            a,b=arr.pop()
            sand[a][b]='.'
        round+=1

print(round)

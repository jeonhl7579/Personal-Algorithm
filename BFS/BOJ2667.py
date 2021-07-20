# 문제 : BOJ2667
# 내용 : 해결

import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
arr=[]

for i in range(N):
    s=list(map(int,input().rstrip()))
    arr.append(s)

#print(arr)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
    
def bfs(x,y):
    arr[x][y]=1
    q=deque()
    q.append((x,y))
    count=0

    while q:
        a,b=q.popleft()
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            if na<0 or na >=N or nb<0 or nb>=N:
                continue        
            if arr[na][nb] == 1:
                arr[na][nb]=0
                count+=1
                q.append((na,nb))

    return count
result=[]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])



   
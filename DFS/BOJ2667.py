# 문제 : BOJ2667
# 내용 : 해결함


import sys
input=sys.stdin.readline

N=int(input())
arr=[]

for i in range(N):
    s=list(map(int,input().rstrip()))
    arr.append(s)

#print(arr)

def dfs(x,y):
    global cnt

    if 0<=x and x<N and 0<=y and y<N:
        if arr[x][y]==1:
            arr[x][y]=0
            cnt+=1
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

result=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            cnt=0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])


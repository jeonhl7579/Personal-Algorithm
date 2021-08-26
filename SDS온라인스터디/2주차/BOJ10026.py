import sys
from collections import deque
input=sys.stdin.readline


def bfs(arr,visit,n,x,y,color):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    q=deque()
    q.append([x,y])

    while q:
        a,b=q.pop()
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            if na<0 or nb<0 or na>=n or nb>=n:
                continue
            if arr[na][nb]==color and not visit[na][nb]:
                visit[na][nb]=True
                q.append([na,nb])

def notsee(arr,visit2,n,x,y,color):
    # R이랑 G는 구분할 필요 없음
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    q=deque()
    q.append([x,y])

    while q:
        a,b=q.pop()
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            if na<0 or nb<0 or na>=n or nb>=n:
                continue
            if color=='R' or color=='G':
                if (arr[na][nb]=="R" or arr[na][nb]=="G") and not visit2[na][nb]:
                    visit2[na][nb]=True
                    q.append([na,nb])
            elif arr[na][nb]==color and not visit2[na][nb]:
                visit2[na][nb]=True
                q.append([na,nb])


def main():
    n=int(input())
    arr=[list(input().strip()) for _ in range(n)]
    visit=[[False]*n for _ in range(n)]
    cnt=0
    # 색약이 없는 사람
    for i in range(n):
        for j in range(n):
            if visit[i][j]==True:
                continue
            bfs(arr,visit,n,i,j,arr[i][j])
            cnt+=1
    print(cnt)
    # 색약이 있는 사람
    visit2=[[False]*n for _ in range(n)]
    cnt2=0
    for i in range(n):
        for j in range(n):
            if visit2[i][j]==True:
                continue
            notsee(arr,visit2,n,i,j,arr[i][j])
            cnt2+=1
    print(cnt2)  
if __name__ =="__main__":
    main()
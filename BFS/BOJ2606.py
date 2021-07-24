import sys
input=sys.stdin.readline

N=int(input())
line=int(input())
arr=[[0]*(N+1) for _ in range(N+1)]
for i in range(line):
    a,b=map(int,input().split())
    arr[a][b]=arr[b][a]=1

visit=[0]*(N+1)

def bfs(V):
    queue=[]
    queue.append(V)
    visit[V]=1
    cnt=0
    while queue:
        a=queue.pop(0)
        #print(a,end=' ')

        for i in range(1,N+1):
            if visit[i]==0 and arr[a][i] ==1:
                queue.append(i)
                visit[i]=1
                cnt+=1
    
    print(cnt)

bfs(1)
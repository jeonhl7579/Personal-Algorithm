import sys
import math

input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
max_result=0
visit=[False]*N
li=[]
result=[]

def backtracking(idx):
    # 최대값
    global max_result

    if idx==N:
        value=0
        for i in range(N-1):
            value+=abs(li[i]-li[i+1])
        result.append(value)
        return
        
    for i in range(N):
        if visit[i]==True:
            continue
        visit[i]=True
        li.append(arr[i])
        backtracking(idx+1)
        li.pop()
        visit[i]=False


backtracking(0)
print(max(result))
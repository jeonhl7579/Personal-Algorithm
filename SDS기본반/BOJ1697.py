import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
max_value=10**5
arr=[0]*(max_value+1)

def bfs():
    q=deque()
    q.append(N)

    while q:
        a=q.popleft()
        if a==K:
            print(arr[a])
            break

        for na in (a+1,a-1,a*2):
            if 0<=na<=max_value and arr[na]==0:
                arr[na]=arr[a]+1
                q.append(na)

bfs()
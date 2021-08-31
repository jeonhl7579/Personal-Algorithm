import sys
input=sys.stdin.readline

n=int(input())
chess=[[False]*n for _ in range(n)]

def backtracking(n,idx):
    # 
    if idx==n:
        return
# 문제 : 백준 1205
# 내용 : ValueError
# 랭킹 리스트, 같은 점수가 있을때는 그러한 점수 들 중에서 인덱스가 작은 등수로 

import sys
input=sys.stdin.readline

N,new_score,P=map(int,input().split())

if N==0:
    print(1)
else:
    score=list(map(int,input().split()))
    if N==P and score[-1]>=new_score:
        print(-1)
    else:
        rank=N+1
        for i in range(N):
            if score[i] <= new_score:
                rank=i+1
                break

        print(rank)
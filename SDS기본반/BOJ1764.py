import sys
input=sys.stdin.readline

N,M=map(int,input().split())

dbj=[]
dic={}

for _ in range(N+M):
    s=input().rstrip()
    # 사전에 s가 없다면
    if s not in dic:
        dic[s]=1
    else:
        dic[s]+=1

for i,j in dic.items():
    if j==2:
        dbj.append(i)

print(len(dbj))
for i in sorted(dbj):
    print(i)

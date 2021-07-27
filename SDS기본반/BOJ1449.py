import sys
input=sys.stdin.readline

N,L=map(int,input().split())
pipe=sorted(list(map(int,input().split())))

#print(pipe)
result=[]

for i in range(N):
    a,b=pipe[i]-0.5,pipe[i]+0.5
    tape_a,tape_b=a,a+L
    if not result:
        result.append([tape_a,tape_b])
    if result[-1][1] >= b:
        continue
    else:
        result.append([tape_a,tape_b])
print(len(result))
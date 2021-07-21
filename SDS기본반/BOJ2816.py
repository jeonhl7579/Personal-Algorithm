import sys
input=sys.stdin.readline

N=int(input())

channel=[]
for i in range(N):
    channel.append(input().rstrip())

#print(channel)
# 화살표 -> 가리키고 있는 채널
idx1,idx2=channel.index('KBS1'),channel.index('KBS2')

if idx1>idx2:
    idx2+=1

print('1'*idx1+'4'*idx1+'1'*idx2+'4'*(idx2-1))
import sys
input=sys.stdin.readline

N=int(input())

room=[]
for _ in range(N):
    room.append(list(map(str,input().rstrip())))

#print(room)
#가로
row=0
#세로
col=0

for i in range(N):
    cnt=0
    for j in range(N):
        if room[i][j] == 'X':
            if cnt >= 2:
                row+=1
            cnt=0
        else:
            cnt+=1
    if cnt >= 2:
        row+=1

for i in range(N):
    cnt=0
    for j in range(N):
        if room[j][i] == 'X':
            if cnt >= 2:
                col+=1
            cnt=0
        else:
            cnt+=1
    if cnt >= 2:
        col+=1

print(row,end=' ')
print(col)
        
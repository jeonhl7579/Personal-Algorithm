import sys
input=sys.stdin.readline

def backtracking(idx,s,arr,visit):
    if idx==6:
        print(*arr)
        return

    for i in range(len(s)):
        if not visit[i]:
            visit[i]=True
            arr.append(s[i])
            backtracking(idx+1,s,arr,visit)
            arr.pop()
            for j in range(i+1,len(s)):
                visit[j]=False

while True:
    li=list(map(int,input().split()))
    if li[0]==0:
        break
    k=li[0]
    s=li[1:]
    result=[]
    visit=[False]*len(s)
    #print(s)
    backtracking(0,s,result,visit)
    print()


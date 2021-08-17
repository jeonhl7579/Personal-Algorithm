import sys
input=sys.stdin.readline

def backtracking(len,idx):
    if len==L:
        v_cnt=0
        con_cnt=0
        for i in range(L):
            if arr[i] in 'aeiou':
                v_cnt+=1
            else:
                con_cnt+=1
        if v_cnt>0 and con_cnt>=2:
            print(''.join(arr))
        return
    
    for i in range(idx,C):
        if not visit[i]:
            arr.append(s[i])
            visit[i]=True
            backtracking(len+1,i+1)
            visit[i]=False
            arr.pop()
            

L,C=map(int,input().split())
visit=[False for i in range(C)]
arr=[]
s=input().split()
s.sort()
backtracking(0,0)

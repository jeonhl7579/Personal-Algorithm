import sys
input=sys.stdin.readline

k=int(input())
sign=input().split()
visit=[False]*10
mx,mn='',''


# 부등호 체크하는 함수
def check(i,j,k):
    if k == '<':
        # 맞으면 True 틀리면 False 반환
        return i<j
    if k == ">":
        return i>j
    return True


def backtracking(idx,s):
    global mx,mn
    if idx==k+1:
        if not len(mn):
            mn=s
        else:
            mx=s
        return
    
    for i in range(10):
        if not visit[i]:
            if idx==0 or check(s[-1],str(i),sign[idx-1]):
                visit[i]=True
                backtracking(idx+1,s+str(i))
                visit[i]=False

backtracking(0,"")
print(mx)
print(mn)



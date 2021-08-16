import sys
input=sys.stdin.readline

k=int(input())
sign=input().split()
mx,mn='',''
# 0부터 9까지 숫자들 중에서 사용했는지 체크해주는 배열
visit=[False]*10

# 체크하는 함수
def check(i,j,k):
    if k=='<':
        return i<j
    if k=='>':
        return i>j
result=[]
# 백트래킹 함수
def backtracking(idx,s):
    global result

    if idx==k+1:
        result.append(s)
        return
    # 0부터 9까지의 숫자 중에서
    for i in range(0,10):
        # 방문하지 않았을 때에
        if not visit[i]:
            if idx==0 or check(s[-1],str(i),sign[idx-1]):
                visit[i]=True
                backtracking(idx+1,s+str(i))
                visit[i]=False

backtracking(0,"")
print(result[len(result)-1])
print(result[0])

import sys
input=sys.stdin.readline

def find(idx,result,a,b,c,d):
    global max_result
    global min_result
    if idx==n:
        # 연산
        max_result=max(result,max_result)
        min_result=min(result,min_result)
        return

    if a:
        find(idx+1,result+set_a[idx],a-1,b,c,d)
    if b:
        find(idx+1,result-set_a[idx],a,b-1,c,d)
    if c:
        find(idx+1,result*set_a[idx],a,b,c-1,d)
    if d:
        find(idx+1,-(-result//set_a[idx])if result<0 else result//set_a[idx],a,b,c,d-1)

max_result=-1
min_result=10**8
n=int(input())
set_a=list(map(int,input().split()))
operator=list(map(int,input().split()))

find(1,set_a[0],operator[0],operator[1],operator[2],operator[3])
print(max_result)
print(min_result)
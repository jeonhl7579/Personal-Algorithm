# 문제 : BOJ 1747
# 내용 : 처음에 문제를 풀었던 방식은 긴 소수 배열을 만들어서 소수들을 찾는 함수,
#        펠린드롬인지 확인하는 함수 이렇게 나누어서 만들었지만
#        n이 1,2인경우를 만들어 주지 않았고, n이 1,000,000일 때에 더 큰 소수이면서 펠린드롬인 수인
#        1003001이 출력되게 해야된다는 것을 간과해서 틀렸던 것 같다.

import sys
import math
input=sys.stdin.readline

def main():
    n=int(input())
    max_n=1000001
    result=0
    for i in range(n,max_n):
        if i==1:
            continue
        if i==2:
            result=i
            break
        # 펠린드롬일때
        if str(i)==str(i)[::-1]:
            if i%2==0:
                continue
            flag=True
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    flag=False
                    break
            if flag:
                result=i
                break
    if result==0:
        result=1003001
    print(result)

if __name__ == "__main__":
    main()
import sys
from itertools import combinations
from string import ascii_lowercase

input=sys.stdin.readline

n,k=map(int,input().split())
words=[]

# difference 함수는 해당되는 인자들을 제외하는 함수인듯
for _ in range(n):
    words.append(set(input().rstrip()[4:-4]).difference('a','c','i','t','n'))

print(words)

except_acitn=set(ascii_lowercase).difference('a','c','i','t','n')
print(except_acitn)

max_cnt=0

if k<5:
    print(0)
else:
    for x in list(combinations(except_acitn,k-5)):
        cnt=0
        for word in words:
            print(word.difference(x))
            if not word.difference(x):
                cnt+=1

        max_cnt=max(max_cnt,cnt)

    print(max_cnt)
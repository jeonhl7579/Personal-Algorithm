import sys
input=sys.stdin.readline

n=int(input())
result_arr=[]
for i in range(n):
    text=input().strip()
    alpha=[0]*26

    for c in text:
        if text.isalpha():
            alpha[ord(c)-ord('a')]+=1
    
    top=max(alpha)

    if alpha.count(top) <2:
        print(chr(ord('a')+alpha.index(top)))
    else:
        print('?')
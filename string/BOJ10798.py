import sys
input=sys.stdin.readline

book=[['']*15 for i in range(5)]

for i in range(5):
    text=list(input().strip())
    for j in range(len(text)):
        book[i][j]=text[j]
print(book)

result=''
for i in range(15):
    for j in range(5):
        if book[j][i] == '':
            continue
        else:
            result+=book[j][i]

print(result)
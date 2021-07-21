# 문제 : 백준 8979
# 내용 : 다른사람코드보고 참고해봤지만 부분성공 나옴 다시 살펴볼것
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
country=[]

for i in range(N):
    country.append(list(map(int,input().split())))

# rank=[0]*N

# for i in range(N):
#     result=(country[i][1]*3)+(country[i][2]*2)+(country[i][3]*1)
#     rank[country[i][0]-1] = result
#     country[i].append(result)

# rank=sorted(list(set(rank)))
# rank.reverse()

# for i in range(N):
#     if K == country[i][0]:
#         print(rank.index(country[i][-1])+1)

# 람다식의 키 리턴값에 -를 붙이면 역순 정렬
country.sort(key=lambda x: (x[1],x[2],x[3]),reverse=True)
#print(country)

# 찾고자 하는 나라의 인덱스 구하기
for i in range(N):
    if country[i][0] == K:
        idx=i

for i in range(N):
    if idx==1:
        continue
    if country[idx][1:] == country[i][1:]:
        print(i+1)
        break

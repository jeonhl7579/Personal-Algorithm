# 난수 생성시키는 라이브러리 
import random

# 단어와 단어 뜻을 저장한 사전
book={'apple':'사과','banana':'바나나','tomato':'토마토','star':'별','time':'시간'}
# 단어를 저장할 리스트
key_book=[]

# 사전에서 key값만 반복시키고 그것을 다 key_book에 저장 시킴
for a in book.keys():
  key_book.append(a)

# 난수 생성 범위를 정해야 하므로
# 사전의 길이 == key_book의 길이
count=len(key_book)
# count수 만큼 False가 요소 값인 리스트(visit)가 생성
visit=[False]*count

while True:
    # visit 리스트에 False가 없다면 문제를 한번씩 다 찾은 것이므로 반복문 종료
    if False not in visit:
        print('문제가 다 출제됬어요!')
        break

    # 난수 생성 부분
    r_num=random.randint(0,count-1)
    # 생성한 난수를 인덱스로 사용 
    if visit[r_num]==False:
        visit[r_num]=True
    elif visit[r_num]==True:
        continue

    print(key_book[r_num]+'의 한글 뜻은 무엇인가요? : ')
    # 값 입력 받고
    s=input().strip()
    # end 입력하면 종료
    if s=='end':
        break
    # 내가 입력 한 값과 사전에서 찾은 value값이 같으면 맞았어요 출력
    elif s==book[key_book[r_num]]:
        print('와! 맞았어요!')
    # 틀리면 땡 출력
    else:
        print('떙!')
  

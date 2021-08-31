import sys
input=sys.stdin.readline

def planting(arr,n,i,j,k):
    fp=[[0,0],[-1,0],[0,1],[1,0],[0,-1]]
    li=[]
    result=0
    for f in [i,j,k]:
        x=f//n
        y=f%n

        for d in range(5):
            nx=x+fp[d][0]
            ny=y+fp[d][1]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            li.append((nx,ny))
            result+=arr[nx][ny]
    # li에 값을 추가할때 []를 넣게 되면 리스트를 추가하는 것이므로
    # unhasable한 값이기 때문에 set으로 바꿔줄떄 오류가 나오게 된다.
    if len(set(li))==15:
        return result
    return 10000

def main():
    n=int(input())
    flower=[]
    fp=[[0,0],[-1,0],[0,1],[1,0],[0,-1]]
    
    for _ in range(n):
        flower.append(list(map(int,input().split())))
    
    min_result=10**8
    for i in range(n**2):
        for j in range(n**2):
            for k in range(n**2):
                min_result=min(min_result,planting(flower,n,i,j,k))

    print(min_result)

if __name__ == "__main__":
    main()
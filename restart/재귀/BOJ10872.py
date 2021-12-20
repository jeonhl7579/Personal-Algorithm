import sys
input=sys.stdin.readline

def factorial(num):
    result=1
    if num>0:
        result=num*factorial(num-1)
    return result

n=int(input())

print(factorial(n))
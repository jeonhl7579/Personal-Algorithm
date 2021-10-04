import sys

sh,sm,ss=map(int,input().split(':'))
eh,em,es=map(int,input().split(':'))

start=sh*60*60+sm*60+ss
end=eh*60*60+em*60+es

if end>start:
    result=end-start
else:
    result=end-start+(24*60*60)

h=result//60//60
m=result//60%60
s=result%60

print("%02d:%02d:%02d"%(h,m,s))
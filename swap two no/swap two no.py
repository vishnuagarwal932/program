a=int(input())
rev=0
while(a>0):
    c=a%10
    rev=rev*10+c
    a//10
 b=int(input())
 rev1=0
 while(b>0):
    d=b%10
    rev1=rev1*10+d
    b=b//10
num1=rev
num2=rev1
swap=num1
num1=num2
num2=swap
print(num1)
print(num2)

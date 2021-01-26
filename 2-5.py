# 輸入三位數，將數字相加123
n=int(input())
# a百b十c個
a=n//100
b=(n%100)//10
c=n%10
# print(a)
# print(b)
# print(c)
print(a+b+c)
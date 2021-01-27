# Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Given a positive integer n, print the nth Fibonacci number.


# 下一個數字=前兩個數字相加
# 印出第n個數字

n=int(input())
a=1
b=1
i=3
while i<=n:
    c=a+b
    a,b=b,c
    i=i+1
if n==1 or n==2:
  print(1)
else:
  print(c,end=" ")




# 印出數列
# n=int(input())
# a=1
# b=1
# print(1,end=" ")
# print(1,end=" ")
# i=3
# while i<n:
#     c=a+b
#     print(c,end=" ")
#     a,b=b,c
#     i=i+1
# Given an integer not less than 2. Print its smallest integer divisor greater than 1.


# 最小因數
n=int(input())
i=2
while i<=n:
  if int(n%i)==0:
    print(i)
    break
  else:
    i=i+1
# For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.

# To do that, you can use the sep and end arguments for the function print().

# 輸入3
n=int(input())
for i in range(n):
  for j in range(0,i+1):
    print(j+1,end="")
  print("")
# For a given integer N, print all the squares of positive integers where the square is less than or equal to N, in ascending order.
# 50
# 1 4 9 16 25 36 49

# 印出小於n2的平方數
n=int(input())
i=1
while i**2<=n:
  print(i**2,end=" ")
  i=i+1

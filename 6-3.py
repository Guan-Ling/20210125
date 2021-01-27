# For a given integer X, find the greatest integer n where 2ⁿ is less than or equal to X. 
# Print the exponent value and the result of the expression 2ⁿ.
# 50
# 5 32 (2^5=32)


import math
n=int(input())
i=1
j=0
while math.pow(2,i)<=n:
  j=i
  i=i+1
print(j,int(math.pow(2,j)))
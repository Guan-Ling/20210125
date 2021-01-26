# In mathematics, the factorial of an integer n, denoted by n! is the following product:

# n! = 1 × 2 × … × n

# For the given integer n calculate the value 

# 1! + 2! + 3! + ... + n!

# Try to discover the solution that uses only one for-loop. And don't use math module in this exercise.

# 階乘相加
n=int(input())
s=0
for i in range(n):
  a=1
  for j in range(0,i+1):
    a=a*(j+1)
  s=s+a
print(s)
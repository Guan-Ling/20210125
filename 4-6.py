# In mathematics, the factorial of an integer n, denoted by n! is the following product:

# n! = 1 × 2 × … × n

# For the given integer n calculate the value n!. Don't use math module in this exercise.


n=int(input())
s=1
for i in range(n):
  s=s*(i+1)
print(s)

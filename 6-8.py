# Given a sequence of non-negative integers, where each number is written in a separate line. 
# The sequence ends with 0. Print the maximum of the sequence.  
# 1 2 3 2 1 0
# 3


# 印到0為止 找出最大的數
n=int(input())
m=0
while n!=0:
  n=int(input())
  if n>m:
    m=n
print(m)
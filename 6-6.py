# Given a sequence of non-negative integers, where each number is written in a separate line. 
# The sequence ends with 0. Print the sum of the sequence.

# 1 7 9 0 
# 17

# 輸入直到0 印出總和
n=int(input())
m=0
while n!=0:
  n=int(input())
  m=m+n
print(m)
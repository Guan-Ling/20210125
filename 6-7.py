# Given a sequence of non-negative integers, where each number is written in a separate line. 
# The sequence ends with 0. Print the average of the sequence. 

# 10 30 0 
# 20.0

# 印到0為止 算平均
n=int(input())
i=0
m=0
while n!=0:
  n=int(input())
  i=i+1
  m=m+n
print(m/(i-1))
# Given a sequence of non-negative integers, where each number is written in a separate line. 
# The sequence ends with 0. Print the index of the first maximum of the sequence.  

# 0之前，找最大的數在哪裡
# 1 7 9 5 0 
# 3

n=int(input())
i=0
m=0
j=0
while n!=0:
  n=int(input())
  if n>m:
    m=n
    j=i
  i=i+1 
print(j+1)
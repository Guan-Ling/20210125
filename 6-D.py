# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. 
# Find how many elements of this sequence are equal to its largest element.

# 0之前，找出最大的數有幾個

n=int(input())
m=n
i=0
while n!=0:
  n=int(input())
  if n==m:
    i=i+1
  if n>m:
    m=n
    i=0
  
print(i+1)
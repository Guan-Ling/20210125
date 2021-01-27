# Given a sequence of non-negative integers, where each number is written in a separate line. 
# The sequence ends with 0. Print the number of elements of the sequence that are greater than their neighbors above.  


# 0之前，找有幾個數字比前一個大
n=int(input())
m=0
i=0
while n!=0:
  n=int(input())
  if n>m:
    i=i+1
  m=n
print(i-1)

# Given a sequence of non-negative integers, where each number is written in a separate line. 
# The sequence ends with 0. Print the number of even elements of the sequence.  


# 0之前，計算有幾個偶數

n=int(input())
i=0
while n!=0:
  n=int(input())
  if n==0:
    break
  if int(n%2)==0:
    i=i+1
print(i)
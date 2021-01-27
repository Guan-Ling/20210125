# Given a list of numbers, print all its even elements. 
# Use a for-loop that iterates over the list itself and not over its indices. 
# That is, don't use range()

# 找出偶數
a=[int(i) for i in input().split()]
for i in a:
  if i%2==0:
    print(i,end=" ")
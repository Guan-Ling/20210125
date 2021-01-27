# Given a list of numbers, find and print all its elements that are greater than their left neighbor.

# 找出比前一個大的數字

a=[int(i) for i in input().split()]
for i in range(len(a)):
  if i!=0 and a[i]>a[i-1]:
    print(a[i],end=" ")
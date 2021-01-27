# Given a list of non-zero integers, find and print the first adjacent pair of elements that have the same sign. 
# If there is no such pair, print 0.

# 同正數或同負數

n=0
a=[int(i) for i in input().split()]
for i in range(1,len(a)):
  if a[i]*a[i-1]>0:
    print(a[i-1],a[i],end=" ")
    n=n+1
    break
if n==0:
  print(0)
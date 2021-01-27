# Given a list of integers, find the first maximum element in it. 
# Print its value and its index (counting with 0).

# 最大數和index

a=[int(i) for i in input().split()]
m=max(a)
for i in range(len(a)):
  if m==a[i]:
    break
print(m,i)

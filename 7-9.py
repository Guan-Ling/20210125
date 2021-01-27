# Given a list of distinct numbers, swap the minimum and the maximum and print the resulting list.

# 最大 最小交換
a=[int(i) for i in input().split()]
x=max(a)
y=min(a)
s=0
t=0

for i in range(len(a)):
  if a[i]==x:
    s=i
  if a[i]==y:
    t=i
a[s],a[t]=y,x

print(a)
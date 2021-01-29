# Given two lists of numbers, count how many numbers of the first one occur in the second one.

# 1 3 2
# 4 3 2

# 2
# 看有幾個重複

a=input().split()
b=input().split()
aa=set(a)
aa=list(aa)
bb=set(b)
bb=list(bb)
c=0
for i in aa:
  for j in bb:
    if i==j:
      c=c+1
print(c)
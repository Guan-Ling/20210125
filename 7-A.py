# Given a list of numbers, count a number of pairs of equal elements. 
# Any two elements that are equal to each other should be counted exactly once.

# 12323  2
# 11111  10

# 算重複幾次

a=[int(i) for i in input().split()]
c=0
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if a[i]==a[j]:
      c=c+1
print(c)
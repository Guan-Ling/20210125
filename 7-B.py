# Given a list of numbers, find and print the elements that appear in it only once. 
# Such elements should be printed in the order in which they occur in the original list.


# 找只有出現過一次的數字
a=[int(i) for i in input().split()]
b=[]
p=[]
for i in range(len(a)):
  c=0
  if a[i] not in p:
    p.append(a[i])
    for j in range(i+1,len(a)):
      if a[i]==a[j]:
        c=c+1
    if c==0:
      b.append(a[i])
print(b)
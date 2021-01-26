# Given three integers, print them in ascending order.


# 給三數排大小
a=int(input())
b=int(input())
c=int(input())
mi=min(a,b,c)
ma=max(a,b,c)

if mi<a<ma:
  print(mi)
  print(a)
  print(ma)
elif mi<b<ma:
  print(mi)
  print(b)
  print(ma)
else:
  print(mi)
  print(c)
  print(ma)
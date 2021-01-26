# Given integer coordinates of three vertices of a rectangle whose sides are parallel to coordinate axes, find the coordinates of the fourth vertex of the rectangle.  

# 找出第四個頂點

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=0
h=0
if b==d:
  h=f
elif b==f:
  h=d
else:
  h=b

if a==c:
  g=e
elif a==e:
  g=c
else:
  g=a
  
print(g)
print(h)

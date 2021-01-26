# Given a string, delete all its characters whose indices are divisible by 3.

# 移除整除三個字
s=input()
l=len(s)
d=""
for i in range(l):
  if i%3!=0:
    d=d+s[i]
print(d)
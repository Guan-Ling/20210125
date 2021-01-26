# Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.


# 給兩個數，只有一個為正數 印YES
a=int(input())
b=int(input())
# c=a+b
# m=max(a,b)
# if c<m:
#   if a>0:
#     print("YES")
#   elif b>0:
#     print("YES")
#   else:
#     print("NO")
# else:
#   print("NO")

if a*b>0:
    print("NO")
else:
    print("YES")
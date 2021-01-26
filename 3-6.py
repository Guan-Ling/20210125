# Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.

#三位數由小到大 印YES
a,b,c=input("three-digit integer:")
if a<b<c:
  print("YES")
else:
  print("NO")
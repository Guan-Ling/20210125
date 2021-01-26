# Let's call an integer a palindrome if it remains the same after reading its digits from right to left. 
# Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise. 

# 輸入四位數，看看是否前後回文 1221 YES
a,b,c,d=input("four-digit integer:")
if int(a)==int(d) and int(b)==int(c):
  print("YES")
else:
  print("NO")
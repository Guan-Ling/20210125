# Write a program that solves a linear equation ax = b in integers. 
# Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.


a=int(input("a:"))
b=int(input("b:"))

if a!=0:
  c=b/a
  c=c*10
  if c%10!=0:
    print("no solution")
  elif c%10==0:
    print(int(c/10))
elif a==0 and b==0:
  print("many solutions")
else:
  print("no solution")
  
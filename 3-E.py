# Given two squares of a chessboard. 
# If they are painted in the same color, print YES, otherwise print NO.
# The program receives four integers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square.

a=int(input("x1:"))
b=int(input("y1:"))
c=int(input("x2:"))
d=int(input("y2:"))

if (a+b)%2==0 and (c+d)%2==0:
  print("YES")
elif (a+b)%2==1 and (c+d)%2==1:
  print("YES")
else:
  print("NO")

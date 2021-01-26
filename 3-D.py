# Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.

# The program receives two integers from 1 to 8 specifying the column and row number of the square.
# 1,1 black 8,8 black

# 黑色 印YES
a=int(input("x:"))
b=int(input("y:"))
if (a+b)%2==0:
  print("YES")
else:
  print("NO")
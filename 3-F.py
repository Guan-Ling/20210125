# Chess king moves one square in any direction. Given two different squares of the chessboard, determine whether a king can go from the first square to the second one in a single move.
# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. 
# The program should output YES if a king can go from the first square to the second one in a single move or NO otherwise.

# 上下左右斜都可移動，總共有8格可以選
a=int(input("x1:"))
b=int(input("y1:"))
c=int(input("x2:"))
d=int(input("y2:"))
x=abs(c-a)
y=abs(d-b)

if x<=1 and y<=1:
  print("YES")
else:
  print("NO")
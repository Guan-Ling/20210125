# Chess queen moves horizontally, vertically or diagonally in any number of squares. 
# Given two different squares of the chessboard, determine whether a queen can go from the first square to the second one in a single move. 

# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. 
# The program should output YES if a queen can go from the first square to the second one in a single move or NO otherwise.

# 八個方位 不限步數
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
a=int(input("x1:"))
b=int(input("y1:"))
c=int(input("x2:"))
d=int(input("y2:"))

if abs(c-a)==abs(d-b) or a==c or b==d:
  print("YES")
else:
  print("NO")

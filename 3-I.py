# Chess knight can move to a square that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally. 
# The complete move therefore looks like the letter L. 
# Given two different squares of the chessboard, determine whether a knight can go from the first square to the second one in a single move.
# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. T
# he program should output YES if a knight can go from the first square to the second one in a single move or NO otherwise.

# 上下左右選一方向 走兩步後，再往走或右走一步
a=int(input("x1:"))
b=int(input("y1:"))
c=int(input("x2:"))
d=int(input("y2:"))

if abs(c-a)==2 and abs(d-b)==1:
  print("YES")
elif abs(c-a)==1 and abs(d-b)==2:
  print("YES")
else:
  print("NO")
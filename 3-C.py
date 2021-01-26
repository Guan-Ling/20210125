# Chess rook moves horizontally or vertically. 
# Given two different squares of the chessboard, determine whether a rook can go from the first square to the second one in a single move.

# The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. 
# The program should output YES if a rook can go from the first square to the second one in a single move or NO otherwise.

# a,b是座標 c,d是往x,y方向移動步數
# 一次只可移鉛直或水平移動(不限步數) 4455 NO
a=int(input("now x:"))
b=int(input("now y:"))
c=int(input("move x:"))
d=int(input("move y:"))

if c==a:
  print("YES")
elif d==b:
  print("YES")
else:
  print("NO")

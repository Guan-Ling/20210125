# It is possible to place 8 queens on an 8×8 chessboard so that no two queens threaten each other. 
# Thus, it requires that no two queens share the same row, column, or diagonal.  

# Given a placement of 8 queens on the chessboard. If there is a pair of queens that violates this rule, print YES, otherwise print NO. 
# The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chessboard with rows and columns numbered from 1 to 8.

# 8皇后問題 直橫斜都不可碰面
k=["a","b","c","d","e","f","g","h"]

for j in range(len(k)):
  # print(k[j])
  k[j]=[int(i) for i in input().split()]
  # print(k[j])
# print(k)


# 斜對角
c=0
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if abs(k[i][0]-k[j][0])==abs(k[i][1]-k[j][1]):
      print("YES")
      c=1
      break
  if c==1:
    break

# 直橫
x=0
y=0
for i in range(len(k)):
  x=x+k[i][0]
  y=y+k[i][1]

s=0
for i in range(8):
  s=s+(i+1)

if c!=1 and x==s and y==s:
  print("NO")
elif c!=1:
  print("YES")







# x = []
# y = []
# for i in range(8):
#   a = [int(s) for s in input().split()]
#   x.append(a[0])
#   y.append(a[1])
# answer = 'NO'
# for i in range(8):
#   for j in range(i + 1, 8):
#     if ((x[i] == x[j]) or
#         (y[i] == y[j]) or
#         (abs(x[i] - x[j]) == abs(y[i] - y[j]))):
#       answer = 'YES'
# print(answer)


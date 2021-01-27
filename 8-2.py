# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, find the maximal element and print its row number and column number. 
# If there are many maximal elements in different rows, report the one with smaller row number. If there are many maximal elements in the same row, report the one with smaller column number. 

# 3 4
# 0 3 2 4
# 2 3 5 5
# 5 1 2 3

# 1 2

# 找第一次出現最大的數字的位置

row,col=[int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(row)]

m=[]
x=0
y=0
m.append(a[0][0])
for i in range(row):
  for j in range(col):
    if a[i][j]>m[0]:
      x=i
      y=j
      m[0]=a[i][j]

print(x,y)

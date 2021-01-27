# Given two positive integers n and m, create a two-dimensional array of size n×m and populate it with the characters "."and "*" in a chequered pattern. 
# The top left corner should have the character "." .


# 6 8
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .



# n=int(input())
# m=int(input())

n,m=[int(i) for i in input().split()]
a=[["."]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j)%2!=0:
            a[i][j]="*"


for row in a:
    print(*row)
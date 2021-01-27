# Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:

# On the main diagonal put 0.
# On the diagonals adjacent to the main put 1.
# On the next adjacent diagonals put 2, and so forth.

# 5

# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0

n=int(input())
a=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j]=abs(i-j)


for row in a:
    print(*row)
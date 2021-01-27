# Given a list of numbers, find and print all its elements with even indices (i.e. A[0], A[2], A[4], ...).

# 找出偶數index的數字

a=[int(i) for i in input().split()]
print(*a[::2])
# Given a list of integers, count how many distinct numbers it has. This task can be solved in a single line.

# 1 2 3 2 1
# 3

a=[int(i) for i in input().split()]
b=set(a)
# print(b)
c=list(b)
print(len(c))
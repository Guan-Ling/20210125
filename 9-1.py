# Given a list of integers, count how many distinct numbers it has. This task can be solved in a single line.

# 1 2 3 2 1
# 3

# 有幾個不重複的數字

a=input().split()
b=set(a)
# print(b)
c=list(b)
print(len(c))


# print(len(set(input().split())))
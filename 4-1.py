# Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

# 印出a~b之間的數字
a=int(input())
b=int(input())
for i in range(a,b+1):
  print(i,end=" ")
# 這樣可以印在同一行
print(*range(a,b+1))
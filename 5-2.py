# Given a string consisting of words separated by spaces. Determine how many words it has. 
# To solve the problem, use the method count.

# 數空白有幾個
n=input()
c=0
for i in n:
  if i==" ":
    c=c+1
print(c+1)
# Given a string that may contain a letter f. Print the index of the first and last occurrence of f. If the letter f occurs only once, then output its index once. If the letter f does not occur, print -1.

# 找第一個f和最後一個f
s=input()

# if print(s.find("f"))==print(s.rfind("f")):
#     print(s.find("f"))
# else:
#     print(s.find("f"),s.rfind("f"))

l=len(s)
c=0
for i in range(l):
  if s[i]=="f":
    print(i,end="")
    c=1
    break

for j in range(l-1,0-1,-1):
  if s[j]=="f":
    if j!=i:
      print(j,end="")
      c=1
      break

if c!=1:
  print("-1")

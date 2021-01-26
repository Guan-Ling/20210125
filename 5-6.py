# Given a string that may contain a letter p. Print the index of the second occurrence of p. 
# If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2.

# 找第二個p 如果只有一個印出-1，如果沒有 印出-2

s=input()
l=len(s)

c=0
for i in range(l):
  if s[i]=="p":
    c=c+1
    if c==2:
      print(i)
if c==1:
  print("-1")
elif c==0:
  print("-2")
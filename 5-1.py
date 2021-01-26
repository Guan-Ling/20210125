# You are given a string.

# In the first line, print the third character of this string.
# In the second line, print the second to last character of this string.
# In the third line, print the first five characters of this string.
# In the fourth line, print all but the last two characters of this string.
# In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
# In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
# In the seventh line, print all the characters of the string in reverse order.
# In the eighth line, print every second character of the string in reverse order, starting from the last one.
# In the ninth line, print the length of the given string.


# 印Abrakadabra
# 答案:
# r
# r
# Abrak
# Abrakadab
# Arkdba
# baaar
# arbadakarbA
# abdkrA
# 11

n=input()
l=len(n)
# 1-印出第二個
print(n[3-1])

# 2-印出倒數第二個
print(n[l-2])

# 3-印出前五個
# print(n[:5])
for i in range(0,5):
  print(n[i],end="")
print("")

# 4-印出全部，最後兩個不印
# print(n[:-2])
for i in range(0,l-2):
  print(n[i],end="")
print("")

# 5-印出全部偶數項
# 0~最後 間隔2
# print(n[0::2])
for i in range(0,l,2):
  print(n[i],end="")
print("")

# 6-印出全部奇數項
# print(n[1::2])
for i in range(1,l,2):
  print(n[i],end="")
print("")

# 7-由後往前印
# print(n[::-1])
for i in range(l-1,0-1,-1):
  print(n[i],end="")
print("")

# 8-由後往前印，每兩個一數
# print(n[::-2])
for i in range(l-1,0-1,-2):
  print(n[i],end="")
print("")

# 9-印出有幾項
# print(len[n])
print(l)
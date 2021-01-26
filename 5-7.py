# Given a string in which the letter h occurs at least twice. 
# Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.

# In the hole in the ground there lived a hobbit
# In tobbit
# 移除兩個h中間的字

s=input()
h1=s.find("h")
h2=s.rfind("h")
print(s[0:h1]+s[(h2+1):len(s)])
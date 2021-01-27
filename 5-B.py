# Given a string in which the letter h occurs at least twice, replace every occurrence of the letter h by the letter H, except for the first and the last ones.
# In the hole in the ground there lived a hobbit
# In the Hole in tHe ground tHere lived a hobbit

# 前後兩h中間的h改成大寫H
s=input()
h1=s.find("h")
h2=s.rfind("h")
k=""
for i in range(h1+1,h2):
  if s[i]=="h":
    k=k+"H"
  else:
    k=k+s[i]
print(s[:h1+1]+k+s[h2:])


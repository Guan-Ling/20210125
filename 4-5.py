# For the given integer N calculate the following sum:

# 1³ + 2³ + ... + N³


n=int(input())
s=0
for i in range(n):
  s=s+(i+1)**3
print(s)

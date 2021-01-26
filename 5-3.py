# Given a string, cut it into two equal parts. If the length of the string is odd, leave the middle character within the first chunk, so that the first string contains one more character than the second. Now print a new string on a single row with the first and second halves swapped: second half first and the first half last.

# Can you solve it without using if?

# 輸入Qwerty
n=input()
l=len(n)

# print(n[l//2:]+n[:l//2])
# print(n[math.ceil(l/2):]+n[:math.ceil(l/2)])


# s = input()
# mid = (len(s) + 1) // 2
# print(s[mid:] + s[:mid])



if l%2==0:
  for j in range(l//2,l):
    print(n[j],end="")
  for i in range(0,l//2):
    print(n[i],end="")
else:
  for j in range(l//2+1,l):
    print(n[j],end="")
  for i in range(0,l//2+1):
    print(n[i],end="")
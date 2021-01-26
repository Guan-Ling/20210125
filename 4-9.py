# There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.

# Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.



# 找出 沒有輸入的數字 5個數 1 2 3 5 

n=int(input())
s=[]
for i in range(n-1):
  a=int(input())
  s.append(a)
for j in range(n):
  count=0
  for k in s:
    if (j+1)==k:
      count=count+1
    
  if count==0:
    print(j+1)
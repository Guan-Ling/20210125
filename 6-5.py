# Given a sequence of non-negative integers, where each number is written in a separate line. 
# Determine the length of the sequence. The sequence ends with 0. Print the length of the sequence (not counting the 0). 
# The numbers following the number 0 should be omitted.

# 1 7 9 0 5 
# 3

# 0之前有幾個數字

n=int(input())
i=0
while n!=0:
  n=int(input())
  i=i+1
print(i-1)

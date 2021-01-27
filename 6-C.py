# Given a sequence of distinct non-negative integers, where each number is written in a separate line. The sequence ends with 0. 
# Print the second largest element in this sequence. 
# It is guaranteed that the sequence has at least two elements.

# 選第二大的數字

k=[]
n=int(input())
k.append(n)
while n!=0:
  n=int(input())
  k.append(n)
k=sorted(k)
print(k[len(k)-2])
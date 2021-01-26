# zeros among the given integers and print it.

# You need to count the number of numbers that are equal to zero, not the number of zero digits.


# 輸入數字 算有幾個0
n=int(input())
sum=0
for i in range(n):
  a=int(input())
  if a==0:
    sum=sum+1
print(sum)

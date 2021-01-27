# Given a list of numbers, determine and print the number of elements that are greater than both of their neighbors.

# The first and the last items of the list shouldn't be considered because they don't have two neighbors.

# 比左右鄰居都大

c=0
a=[int(i) for i in input().split()]
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        c=c+1
    if len(a)==2:
      break
print(c)
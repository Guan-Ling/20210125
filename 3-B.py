# Given three integers, in which two are equal to each other and the third one is different. 
# Print the order number of this different one - 1, 2 or 3.

a=int(input("first:"))
b=int(input("second:"))
c=int(input("third:"))

if a==b or b==c or a==c:
  if a==b:
    print(3)
  elif b==c:
    print(1)
  elif a==c:
    print(2)
# Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.

# 輸入月份 輸出天數
n=int(input("month:"))
if n==2:
  print(28)
elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
  print(31)
else:
  print(30)
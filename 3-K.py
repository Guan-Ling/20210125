# Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, print the month and the day of the next day to it.

# 天數+1
m=int(input("month:"))
n=int(input("day:"))

if m==2 and n==28:
  m=m+1
  n=1
elif n==30:
  if m==2 or m==4 or m==6 or m==9 or m==11:
    m=m+1
    n=1
  else:
    n=n+1
elif n==31:
  if m==1 or m==3 or m==5 or m==7 or m==8 or m==10:
    m=m+1
    n=1
  elif m==12:
    m=1
    n=1
  else:
    n=n+1
else:
  n=n+1
print(m)
print(n)
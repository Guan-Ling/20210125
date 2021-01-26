# Given a year (as a positive integer), find the respective number of the century. Note that, for example, 20th century began with the year 1901. 
# 給西元年份，算出幾世紀，1901-2000是20世紀
n=int(input())

# print((n-1)//100+1)

if n%100==0:
  print(n//100)
else:
  print(n//100+1)
# As a future athlete you just started your practice for an upcoming event. On the first day you run x miles, and by the day of the event you must be able to run y miles.

# Calculate the number of days required for you to finally reach the required distance for the event, if you increases your distance each day by 10% from the previous day.

# Print one integer representing the number of days to reach the required distance.

# 10 30
# 13

# 每天增加前一天的10% 幾天之後可以達到目標
# 輸入現在/目標
a=int(input())
b=int(input())

i=1
while (1.1*a)<b:
  i=i+1
  a=1.1*a
  # print(a)
if a>=b:
  print(i)
else:
  print(i+1)

# m=0
# i=1
# while m<b:
#     m=m*1.1
#     i=i+1
# print(i)
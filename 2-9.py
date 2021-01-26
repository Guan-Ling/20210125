# 100 cents=1 dollar
# D=dollar, C=cent, n=number of cake
D=int(input())
C=int(input())
n=int(input())
DC=n*(D*100+C)
print(DC//100," ",DC%100)
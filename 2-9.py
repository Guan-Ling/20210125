# A cupcake costs A dollars and B cents. 
# Determine, how many dollars and cents should one pay for N cupcakes. 
# A program gets three numbers: A, B, N. 
# It should print two numbers: total cost in dollars and cents.

# 100 cents=1 dollar
# D=dollar, C=cent, n=number of cake
D=int(input())
C=int(input())
n=int(input())
DC=n*(D*100+C)
print(DC//100," ",DC%100)
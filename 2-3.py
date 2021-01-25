# 輸入大於9的數字 取最後兩位
n=input()
l=len(n)
#print(int(n)//(10**(l-1)))
R=int(n)%10
RR=(int(n)%100)//10
print(RR*10+R)
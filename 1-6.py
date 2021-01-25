s=int(input())
h=int((s/60)/60)
m=int(s/60)
ss=s-(h*60*60)-(m*60)
print(h," ",m)

#方法二
print(s//3600,s//60,s%60)
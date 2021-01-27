# Given a list of numbers with all elements sorted in ascending order, determine and print the number of distinct elements in it.

# 找有幾個不同的數字
#set 自動把重複拿掉


a=[int(i) for i in input().split()]
print(set(a))
print(len(set(a)))

b=[]
c=0
for i in a:
    if i not in b:
        b.append(i)
        c=c+1
print(c)
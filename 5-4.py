# Given a string consisting of exactly two words separated by a space. Print a new string with the first and second words swapped: the second word is printed first. Consider all adjacent non-space characters a single word.

# Can you solve it without using if-else and loops?


# input:Hello, world!
# output:world! Hello,


s=input()
# 找空格k
k=s.find(" ")

print(s[k+1:],s[:k])
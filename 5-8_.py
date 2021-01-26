# Given a string in which the letter h occurs at least twice, reverse the sequence of characters enclosed between the first and last occurrences of it.
# In the hole in the ground there lived a hobbit
# In th a devil ereht dnuorg eht ni eloh ehobbit


s=input()
h1=s.find("h")
h2=s.rfind("h")
# print(h1)
# print(h2)
print(s[:h1]+s[h2:h1:-1]+s[h2:])
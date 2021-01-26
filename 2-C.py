# The hour hand of an analog clock turned α degrees since the midnight. 
# Determine the angle by which the minute hand turned since the start of the current hour. 
# Input and output in this problems are integers.


# 給時針角度，算出分針角度
# n時針角度
n=int(input())

# nn現在時間(用分鐘算)
nn=int(n/(360/12/60))
# print(nn)
# 用分鐘換算分針角度
nnn=int((nn%60)*(360/60))
print(nnn)
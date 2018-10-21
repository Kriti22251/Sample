'''from datetime import datetime
s1 = int(input())
s2 = '11:03:11' # for example
format = '%H:%M'
time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
print time'''
hr1,min1=input().split()
hr2,min2=input().split()
hr3=int(hr1)-int(hr2)
min3=int(min1)-int(min2)
print(abs(hr3),abs(min3))

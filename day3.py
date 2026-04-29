-------multiplication table from 1 to 10 in a formatted grid-------
for i in range(1,11):
    for j in range(1,11):
        print("{:02d}".format(i*j),end=" ")
    print()
  

--------password--------
a=input("enter a password:")
up=0
lc=0
sp=0
dg=0
if len(a)>7:
    for i in a:
        if i.isupper():
            up+=1
        elif i.islower():
            lc+=1
        elif i.isdigit():
            dg+=1
        else:
            sp+=1
    if( up>0 and lc>0 and sp>0 and dg>0):
        print("STRONG")
    else:
        print("WEAK")
else:
    print("WEAK DUE TO LESS NUMBER OF CHARACTERS")


-------digital clock that displays time in hours, minutes, and seconds----
:DIGITAL CLOCK
import time
import sys
h=3
m=59
s=0
while True:
    sys.stdout.write("\r{0:2d} : {1:2d} : {2:2d}".format(h,m,s))
    sys.stdout.flush()
    time.sleep(1)
    s=s+1
    if s==60:
        s=0
        m=m+1
    if m==60:
        m=0
        h=h+1
    if h==13:
        h=1


-------different countries time--------
from datetime import datetime
import pytz
a=pytz.timezone("Asia/Tokyo")
b=datetime.now(a)
print(b)
for i in pytz.all_timezones:
  print(i)

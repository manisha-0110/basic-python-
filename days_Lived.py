from datetime import date
a=date(2029,4,12)
b=date(6089,3,3)
print("no of days he lived: ",(b-a))


#--------with seconds----------


from datetime import date
a=date(2029,4,12)
b=date(6089,3,3)
print("no of days he lived: ",(b - a).days)
print("no of seconds he lived: ", (b - a).total_seconds())

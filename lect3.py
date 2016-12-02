from datetime import datetime
now = datetime.now()
min = now.minute
green = 3
rad = 2
t = 5
x = min % t
if x <= green:
    print ("green")
elif x >= rad:
    print ("rad")
print (x)

a = (2, 7)
b = (6, 1)
c = (12, 5)



v = [int(e) for e in input('v = ').split()] #ใส่ค่าเท่าไหร่ก็ได้
u = [int(e) for e in input('u = ').split()]
a = 0
for i in range(len(v)): #หาขนาดของ v
    a += u[i]*v[i]
print((str)(a))
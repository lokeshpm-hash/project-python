a=1
b=1.0
c="loki"
d=True
sales = [12000, 0, 8500, 15000, -200, 9800]
f=(1,2,3,4)
g={1,2,3,"loki"}
h={"name":"loki","age":23}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(sales))
print(type(f))
print(type(g))
print(type(h))
total=0
for sale in sales:
    if sale<=0:
        print("skipped invalid values",sale)
        continue
    total+=sale
    print("Added ",sale,"total",total)
    
    if total>30000:
        break

if total>=30000:
    print("Target Reached Stopped at",total)
else:
    print("Target not Reached")
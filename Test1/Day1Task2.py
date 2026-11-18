prices = [500, 1200, 800, 2500, 300]


def apply_discount(price, discount=10):
    return price-(price*discount/100)


def total(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
      
gst=list( map(lambda x:x*1.18,prices))
above=list(filter(lambda x:x>=1000,prices))
below=list(filter(lambda x:x<1000,prices))


print("After Discount -> ",apply_discount(1000))
print("After Discount -> ",apply_discount(1000,25))
print("Total value of list -> ",total(5,10,15))
print("Above 1000: ",above)
print("With Gst: ",gst)
print("Below 1000 :",below)
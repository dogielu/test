def my_range(x):
    a=0
    while a<x:
        yield a
        a+=1
for x in my_range(20):
    print(x)

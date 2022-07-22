n=[1,3,4,5,6,7,5,88,8,88,9,9,0,1,3]
for i in n:
    k=n.count(i)
    if k>1:
        n.remove(i)
print(n)




mat=[[1,2,3],[4,5,6],[7,8,9]]
l=[]
k=1234
for items in mat:
    print(items)
for x in mat:
    for y in x:
        l.append(y)
    print(l)
numbers=[1,2,34,5]
num=(1,2,3) #it is tupple its values cannot be changed
h,r,t,e=numbers
print(h,r,t,e)
j=[]
numbers.append(6)
numbers.insert(2,8)
numbers.sort()
numbers.reverse()
k=numbers.copy()
print(k)
j.append(6)
print(numbers)
print(j)
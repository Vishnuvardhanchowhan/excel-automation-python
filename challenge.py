no_x = [5,2,5,2,2]
numbers=[3,4,56,67,89,34,8632,8338,33,1241,3121,121223,442]
for y in no_x:
    out=''
    for count in range(y):
        out+='x'
    print(out)
numbers_r=numbers
for i in range(len(numbers)-1):
    if numbers[i]>=numbers[i+1]:
        grt_num=numbers[i]
        numbers[i+1]=grt_num
    else:
        grt_num=numbers[i+1]
print(grt_num)
print(numbers_r)
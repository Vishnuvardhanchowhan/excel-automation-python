h_price=1000000
verify=True
verify2=True
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(total)
for items in "vishnu":
    print(items)
for items2 in range(6):
    print(items2)
for lists in ["harsha","vishnu","babu"]:
    print(lists)

while(verify):
    Name = str(input("Please enter your full name:"))
    if len(Name)<3 :
        print(f'your Name is too short add {3-len(Name)} letters to it.')
    elif len(Name)>25 :
        print(f'your Name is too long reduce {len(Name)-10} letters to it.')
    else :
        print(f'your name is {len(Name)} letters long , '
              f'looks good you can proceed further. ')
        verify = False
weight=int(input('what is your weight :'))
while(verify2):
    unit = input("select your units as eigther Lbs or Kgs :")
    if unit=="Lbs":
        print(f'you are {weight*0.45} Kgs')
        verify2=False
    elif unit=="Kgs":
        print(f'you are {weight/0.45} Lbs')
        verify2=False
    else:
        print("select correct units!")



credit=int(input("what is your credit score :"))
income=int(input("what is your annual income :"))
criminal_record=bool(input("Do you have any criminal record :"))

if  credit >=100000:
    print("you need to put down 10% that is", h_price / 10, "$")
else:
    print("you need to put down 20% that is", h_price / 5, "$")
if (income>=400000 or credit >=100000) and not criminal_record:
    print("Congrats! you are eligible for applying loan upto $2000000 :)")
elif (income >= 100000 or credit >= 50000) and not criminal_record:
        print("Congrats! you are eligible for applying loan upto $1000000 :) ")
else:
    print('sorry! we cant process your request for loan as you are not eligible'
          ':( , better luck next time!' )
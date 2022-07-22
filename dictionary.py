get_inp=input("phone number:")
print(get_inp.split())
out=""
num={
"1":"one ",
"2":"two ",
"3":"three ",
"4":"four ",
"5":"five ",
"6":"six ",
"7":"seven ",
"8":"eight ",
"9":"nine ",
"0":"zero ",
}
for i in get_inp:
    out=out+num.get(i,"!")
print(out)
client={
    "name":"vishnu",
"age":30,
"verify_stat":True
}
print(client["name"])
print(client.get("birthdate","28 sept 2002"))
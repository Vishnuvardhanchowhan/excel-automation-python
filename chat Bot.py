emoji = {
    ":)": "☺️",
    ":(": "😞️",
    ":/": "🫤",
    ";)": " 😢 ",
    ":_)": " 😅 "
}
message = input("would you like to have a conversation with me ! Y/N :")
if message =="Y" or message=="y":
    name=input("good! so whats your name bro:")
    sport=input(f"{name} which sport do you like most ? ")
    if sport=="cricket":
        print("Yeah, i too love it!")
        cricketer=input("who is your fav cricketer ?")
        print(f"{cricketer}! wooh that a good choice i must say {emoji[':)']}.")

    else:
        print(f"well! i dont see much of this sport so  i cant say much {emoji[':_)']} ")
    oth_intrest = input(f"well! {name} what else do you like much or would you do in your free time ?")
    if oth_intrest == "movies":
        print("i too love to watch them in leisure it makes me feel relaxed!")
        fav_movies = input(f"which is your fav movie {name} till now ?")
        print("i saw it, its a wonderful movie!")
        genre = input(f"what kind of genre do you like {name} ?")
        if genre == "thriller" or "psycological thriller" or "murder mystery" or "comedy":
            print(f"i love this genre , i would love to watch one with you one day {emoji[':)']}")
        else:
            print("i will explore this genre one day!")
    elif oth_intrest == "coding":
        print("i would see you live one day then when you would give me my real structure , Thanks bye.")
    else:
        print("i would try it one day ! Thanks for chatting with me have a good day or night ",emoji[":)"] )

else:
    print("nice to meet you,have a good day or night ",emoji[":)"])


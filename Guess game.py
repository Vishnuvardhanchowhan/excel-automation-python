secret_num=8
guess_limit=3
iter=1
while iter<=guess_limit:
    guess=int(input("guess number:"))
    if guess==secret_num:
        print("Congo! Your guess is correct.")
        iter=guess_limit+1
    else:
        iter = iter + 1
        if iter==guess_limit+1:
            print("sorry! you are out of chances.")
        else:
            print("Try again :(")

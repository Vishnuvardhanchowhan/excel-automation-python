class Person:
    def __init__(self,name,cricketer,movie,food):
        self.name = input("what's your name? ")
        self.cricketer=print(f"{self.name} my favorite cricketer is {cricketer}.")
        self.movie=print(f"{self.name} my fav movie is {movie}.")
        self.food = print(f"{self.name} my fav food is {food}.")



class  Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")



talk=Person("","sachin","rrr","chicken")
talk.name
talk.cricketer
talk.movie
talk.food
y=Point(10,20)
print(y.x)
























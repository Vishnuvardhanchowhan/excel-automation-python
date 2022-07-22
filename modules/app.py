from pathlib import Path
path = Path("omg")
path.rmdir()

import random


class Dice:
    def __init__(self):
        self.x = random.randint(1, 6)
        self.y = random.randint(1, 6)


roll = Dice()
tup = (roll.x, roll.y)
print(tup)




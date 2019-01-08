import random

codelen = 2
widthRoom = 9
assert widthRoom % 2 == 1, "Room width must be an odd number!!!"
rarityRoom = 10
rarityRoom = int((rarityRoom / 100) * 26 ** codelen)

rooms = []


class roomClass:
    def __init__(self):
        self.code = ""
        self.contents = [[None for _ in range(widthRoom)] for _ in range(widthRoom)]
        self.populate()
        self.generatecode()

    def generatecode(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.code = ""
        for _ in range(codelen):
            self.code += random.choice(letters)

    def populate(self):
        for _ in range(random.randint(1, 50)):
            self.contents[random.randint(0, widthRoom - 1)][random.randint(0, widthRoom - 1)] = monsterClass()

    def printRoom(self):
        for x in self.contents:
            for y in x:
                if y is not None:
                    if type(y) == playerClass:
                        print(y.name[0].capitalize(), end=" ")
                    else:
                        print(y.name[0].lower(), end=" ")
                else:
                    print(end="_ ")
            print()

    def getCoords(self, occupant):
        for x in self.contents:
            for y in x:
                if y == occupant:
                    return self.contents.index(x), x.index(y)
        return None


class playerClass:
    def __init__(self):
        self.health = 10
        self.name = input("What's your name? ")
        self.password = input("What's your secret code? ")
        self.room = None

    def enterRoom(self, room):
        self.room = room
        perimeter = random.randint(0, widthRoom ** 2)
        while perimeter % widthRoom != 0 and not (perimeter < widthRoom or perimeter > widthRoom ** 2 - widthRoom):
            perimeter = random.randint(0, widthRoom ** 2)
        x, y = divmod(perimeter, widthRoom)
        self.room.contents[y][x] = self


class monsterClass:
    def __init__(self):
        self.health = random.randint(1, 10)
        self.name = random.choice(["Marauder", "Zombie", "Skeleton", "Pirate"])


def search():
    if len(action) == codelen and player.room is None:
        for room in rooms:
            if room.code == action:
                print(f"You entered room {room.code}")
                player.enterRoom(room)
                break
    elif len(action) == codelen and player.room is not None:
        print("You cannot search while you are still in a room...\n")


def look():
    if action in ["look"]:
        if player.room is not None:
            player.room.printRoom()
        else:
            print("You are not in a room!\n")


def leave():
    if action in ["leave"]:
        if player.room is not None:
            x, y = player.room.getCoords(player)
            if x == (widthRoom + 1) / 2 and x == (widthRoom + 1) / 2:
                player.room = None
                print(f"You left room {player.room.code}... \n")
            else:
                print("You must be in the center of the room to leave.")


for _ in range(rarityRoom):
    rooms.append(roomClass())

player = playerClass()
print(rooms[0].code, "\n")
prompt = "input: "
action = input(prompt).lower()
while action != "quit":
    search()
    look()
    leave()

    action = input(prompt).lower()

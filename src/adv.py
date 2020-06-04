from room import Room
from player import Player
from item import Item

# Declare all the rooms


def introduction():
    print("Welome, you're our new explorer, let's start off by introducing yourself. What is your name?")
    name = input("")
    print("Hello, " + name +", you are vacationing on an island talking a random walk around and stumble on an old abandoned house. You decide to walk around. See if you can find any treasure.")
    return name

items = {
    'sword': Item('sword', 'A normal sword'),
    'rocks': Item('rocks', 'a handful of hard rocks'),
    'dagger': Item('dagger', 'a rusty dagger'),
    'spoon': Item('spoon', 'a silver spoon that is probably worth a little bit of coin'),
    'jar': Item('jar', 'a jar of oil of some sort')
}

# is a repl a special thing
# how do room and player class connect

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[items['rocks']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[items['rocks']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['dagger'], items['spoon']])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = introduction()
current_room = room['outside']
player1 = Player(name)
print("Hello", player1.name)
while True:
    print(current_room.name, current_room.desc, ".You see", current_room.items, 'near you.')
    cmd = player1.getInput()
    try:
        if cmd == "n":
            print("Going north")
            current_room = current_room.n_to
        if cmd == "e":
            print("journeying east")
            current_room = current_room.e_to
        if cmd == "s":
            print("travelling south")
            current_room = current_room.s_to
        if cmd == "w":
            print("heading west")
            current_room = current_room.w_to
        if cmd == 'get':
            print("adding", current_room.items, "to inventory")
            player1.getItem(current_room.items) 
        if cmd == 'inventory':
            print("Your inventory includes:", player1.items)
            
    except: 
        print("Can't travel further in that direction")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

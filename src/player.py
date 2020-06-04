# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
  def __init__(self, name, room, items=[],rank="novice"):
    self.name = name
    self.rank = rank
    self.items = items
    self.room = room

  def __str__(self):
    return "{name}"

  def getInput(self):
    cmd = input(">>> ")
    if cmd=="q":
      exit()
      print("Goodbye {self.name}")
    if cmd=="h":
      print("Help: Press n for north, e for east, w for west and s for south. press q to quit")
    if cmd=="n":
      return "n"
    if cmd=="s":
      return "s"
    if cmd=="e":
      return "e"
    if cmd=="w":
      return "w"
    if cmd=="inventory":
      return "inventory"
    if cmd=="get":
      return "get"
    if cmd=="search":
      return "search"
  def getItem(self, item):  
    print("item", item)
    self.items = self.items + item
  def dropItem(item):
    self.items -= item

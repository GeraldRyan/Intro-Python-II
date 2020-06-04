# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name="link", rank="novice", items=''):
    self.name = name
    self.rank = rank
    self.items = items

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
  def getItem(self, item):  #why is this not being called???????????????????????????))))))))
    print("item", item)
    self.items = self.items + item
  def dropItem(item):
    self.items -= item

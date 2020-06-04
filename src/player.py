# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name="link", rank="novice"):
    self.name = name
    self.rank = rank

  def __str__(self):
    return "{name}"

  def play(self):
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


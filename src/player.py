# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name="link", rank="novice"):
    self.name = name
    self.rank = rank

  def __str__(self):
    return "{name}"

  def move(self,cmd):
    if cmd=="n":
      print("Helo N")
      exit()
    if cmd=="s":
      exit()
    if cmd=="e":
      exit()
    if cmd=="w":
      exit()
    if cmd=="q":
      print("Goodbye {self.name}")
      exit()
  def play(self):
    cmd = input(">>>")
    self.move(cmd)


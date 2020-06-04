# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
  def __init__(self, name, desc, items=None):
    self.name = name
    self.desc = desc
    if items == None:
      self.items = []
    else:
      self.items = items



  def __str__(self):
    return "{self.name}, {desc}"

  def printItems(self):
    for item in self.items:
      print(f"You look around and see {item.name}, {item.desc}")

# TODO Get items
  # def getItem(self, item):  
  #   print("item", item)
  #   self.items = self.items + item
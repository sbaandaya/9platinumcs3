class Animal:
  def __init__(self, name):
    self.name = name
  def eat(self):
    print(self.name, "is eating something")
  def make_sound(self):
    print(self.name, "is making some noise")
class Lion(Animal):
  def eat(self):
    print(self.name, "eats fresh meat.")
  def make_sound(self):
    print(self.name, "roars loudly!")
class Elephant(Animal):
  def eat(self):
   print(self.name, "eats grass and fruits.")
  def make_sound(self):
    print(self.name, "trumpets!")
class Monkey(Animal):
  def eat(self):
    print(self.name, "eats bananas.")
  def make_sound(self):
    print(self.name, "chatters!")

Lion1 = Lion("Lion")
Elephant1 = Elephant("Elephant")
Monkey1 = Monkey("Monkey")

animals = [Lion1, Elephant1, Monkey1]
for animal in animals:
  animal.make_sound()
  animal.eat()
  print("-----")

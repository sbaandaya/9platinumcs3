print("1. (a) Duck typing as explained in the video, is another way to achieve inheritance.")
print("1. (b) The method that Car needed to function in the same loop as Dog and Cat is the method speak")
print("")

class Car:
  def move(self):
    print("The car drives on the road.")

class Boat:
  def move(self):
    print("The boat sails on water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

vehicle = [Car(), Boat(), Drone()]
for start_trip in vehicle:
  start_trip.move()

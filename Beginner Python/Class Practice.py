import time

class Robot():
   def __init__(self, pick, place, location, max_speed, min_speed, time, start):
      self.pick = pick
      self.place = place
      self.location = location
      self.max_speed = max_speed
      self.min_speed = min_speed
      self.time = time
      self.start = start

   def move(self, choice, item, location):
      if choice == "pick":
         print("Beep, boop. I will pick up the {} from the {}".format(item, location))
      elif choice == "place":
         print("Beep, boop. I will place the {} over on the {}".format(item, location))

   def speed(self, max_speed, min_speed):
      if int(max_speed) >= 100:
         print("Just keep in mind that {} speed is quite fast".format(max_speed))
      if int(min_speed) < 0:
         print("Beep, boop. Min speed cannot be {}".format(min_speed))
      if int(max_speed) < 100 and int(min_speed) > 0:
         print("Setting speed parameters: ")
         time.sleep(2)
         print("Max speed: {}".format(max_speed))
         time.sleep(2)
         print("Min speed: {}".format(min_speed))
         time.sleep(3)
         print("Beep, boop....Speed settings complete")

   def motion(self, timer, start):
      if start == 's':
         print("Starting the motion")
         run_time = time.sleep(int(timer))
         print("Beep, boop! Motion complete!")
      else:
         print("BEEEPPPP! Invalid command! Robot has failed...")

action = input("Would you like to pick or place?: ")
item = input("What would you like to {}: ".format(action))
max_speed = input("What do you want your max speed to be?: ")
min_speed = input("What do you want your min speed to be?: ")

if action == "place":
   loc = input("Where am I placing the {}: ".format(item))
else:
   loc = input("Where am I picking the {} from?: ".format(item))

timer = input("How many seconds do you want the robot to run?: ")
start = input("Parameters are ready to go! Please press 'S'!: ")

user = Robot(action, item, loc, max_speed, min_speed, time, start)
user.move(action, item, loc)
user.speed(max_speed, min_speed)
user.motion(timer, start)

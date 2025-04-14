import random
import time

class Car:
  def __init__(self, direction):
    self.direction = direction
    self.position = 0

class TrafficLight:
  def __init__(self):
    self.color = "red"

  def change_color(self):
    if self.color == "red":
      self.color = "green"
    else:
      self.color = "red"

# ... (rest of the simulation logic) ...
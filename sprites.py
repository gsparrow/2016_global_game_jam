# -*- coding: utf-8 -*-
# vim: nu cursorline foldmethod=marker
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent

import pygame

class my_sprite: # {{{
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier):
    self.my_x = x
    self.my_y = y
    self.my_velocity_x = velocity_x
    self.my_velocity_y = velocity_y
    if size_multiplier < 2:
      self.size = 2
    else:
      self.size = size_multiplier

  def get_x (self):
    return self.my_x
  def get_y (self):
    return self.my_x
  def get_velocity_x (self):
    return self.my_velocity_x
  def get_velocity_y (self):
    return self.my_velocity_y
  def get_size_multiplier (self):
    return self.size

  def set_x (self, x):
    self.my_x = x
  def set_y (self, y):
    self.my_y = y
  def set_velocity_x (self, velocity_x):
    self.my_velocity_x = velocity_x
  def set_velocity_y (self, velocity_y):
    self.my_velocity_y = velocity_y
  def set_size_multiplier (self, size):
    self.size = size
# }}}

class bubble(my_sprite):
  def __init__(self, x, y, radius, velocity_x, velocity_y, color, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, 1)
    self.radius=radius
    self.screen = screen
    self.color = color
    self.active = True
  
  def get_radius(self):
    return self.radius

  def draw(self):
    if (self.active):
      pygame.draw.circle(self.screen, self.color, (self.my_x, self.my_y), self.radius, 0)
    else:
      pass

  def pop(self):
    self.active=False

  def move(self, MAXX, MAXY):
    if (self.my_x + self.my_velocity_x - self.radius) < 0 or (self.my_x + self.my_velocity_x + self.radius) > MAXX:
      self.my_velocity_x = -1*self.my_velocity_x
    self.my_x = self.my_x + self.my_velocity_x
    if (self.my_y + self.my_velocity_y - self.radius) < 0 or (self.my_y + self.my_velocity_y + self.radius) > MAXY:
      self.my_velocity_y = -1*self.my_velocity_y
    self.my_y = self.my_y + self.my_velocity_y

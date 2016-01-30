# -*- coding: utf-8 -*-
# vim: nu cursorline foldmethod=marker
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent

#!/usr/bin/python

import sys
import pygame
import sprites
from math import pi
import random

pygame.init()
BUBBLES = 5
RADIUS = 50
WIDTH = 700										# arbitrary values for now
HEIGHT = 700
size = WIDTH, HEIGHT
WHITE      = (255, 255, 255)			      					#a few predefined constant colors
BLACK      = (  0,   0,   0)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)
GREY       = (128, 128, 128) 
YELLOW     = (255, 255,   0)
PINK       = (255, 192, 203)
LBLUE      = (191, 238, 244)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ritual")

done = False
clock = pygame.time.Clock()
rndi = random.SystemRandom().randint

my_bubbles = [sprites.bubble(rndi(RADIUS,WIDTH-RADIUS),rndi(RADIUS,HEIGHT-RADIUS), RADIUS, rndi(1,10), rndi(1,10), WHITE, screen)
              for _ in range(BUBBLES)]
while not done:

  #limit the clock to ten loops per second
  clock.tick(20)

  for event in pygame.event.get():							#allows you to exit by clicking x
    if event.type == pygame.QUIT:
      done =True
    if event.type == pygame.MOUSEBUTTONUP:                                              #pops the bubble if you click within the square
      pos = pygame.mouse.get_pos()                                                      #created by using its radius as lengths
      [bubble.pop() for bubble in my_bubbles if bubble.contains(pos)]
    if event.type == pygame.KEYDOWN:
      key = pygame.key.get_pressed()
      if key[pygame.K_q] or key[pygame.K_x]:
        done = True

  screen.fill(WHITE)
  ### draw bathroom wall {{{
  ###  0 ### {{{
  pygame.draw.rect(screen, GREY, [2, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [20, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [20, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [7, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [20, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (24,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [52, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [102, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [120, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [120, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [107, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [120, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (124,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [152, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [202, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [220, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [220, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [207, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [220, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (224,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [252, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [302, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [320, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [320, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [307, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [320, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (324,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [352, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [402, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [420, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [420, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [407, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [420, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (424,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [452, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [502, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [520, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [520, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [507, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [520, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (524,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [552, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [602, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [620, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [620, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [607, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [620, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (624,24), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [652, 2, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [702, 2, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [720, 20, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [720, 5, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [707, 20, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [720, 20, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (724,24), 7)
  # }}}
  # }}}
  ###  1 ### {{{
  pygame.draw.rect(screen, GREY, [2, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [52, 52, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [70, 70, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 55, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [57, 70, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 70, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (74,74), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [102, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [152, 52, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [170, 70, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 55, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [157, 70, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 70, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (174,74), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [202, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [252, 52, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [270, 70, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 55, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [257, 70, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 70, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (274,74), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [302, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [352, 52, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [370, 70, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 55, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [357, 70, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 70, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (374,74), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [402, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [452, 52, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [470, 70, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 55, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [457, 70, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 70, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (474,74), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [502, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [552, 52, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [570, 70, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 55, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [557, 70, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 70, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (574,74), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [602, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [652, 52, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [702, 52, 50, 50], 5)
  # }}}
  ###  2 ### {{{
  pygame.draw.rect(screen, GREY, [2, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [20, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [20, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [7, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [20, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (24,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [52, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [102, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [120, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [120, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [107, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [120, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (124,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [152, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [202, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [220, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [220, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [207, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [220, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (224,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [252, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [302, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [320, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [320, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [307, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [320, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (324,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [352, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [402, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [420, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [420, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [407, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [420, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (424,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [452, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [502, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [520, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [520, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [507, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [520, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (524,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [552, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [602, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [620, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [620, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [607, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [620, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (624,124), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [652, 102, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [702, 102, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [720, 120, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [720, 105, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [707, 120, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [720, 120, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (724,124), 7)
  # }}}
  # }}}
  ###  3 ### {{{
  pygame.draw.rect(screen, GREY, [2, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [52, 152, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [70, 170, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 155, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [57, 170, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 170, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (74,174), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [102, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [152, 152, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [170, 170, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 155, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [157, 170, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 170, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (174,174), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [202, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [252, 152, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [270, 170, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 155, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [257, 170, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 170, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (274,174), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [302, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [352, 152, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [370, 170, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 155, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [357, 170, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 170, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (374,174), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [402, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [452, 152, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [470, 170, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 155, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [457, 170, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 170, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (474,174), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [502, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [552, 152, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [570, 170, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 155, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [557, 170, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 170, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (574,174), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [602, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [652, 152, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [702, 152, 50, 50], 5)
  # }}}
  ###  4 ### {{{
  pygame.draw.rect(screen, GREY, [2, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [20, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [20, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [7, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [20, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (24,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [52, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [102, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [120, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [120, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [107, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [120, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (124,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [152, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [202, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [220, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [220, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [207, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [220, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (224,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [252, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [302, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [320, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [320, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [307, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [320, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (324,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [352, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [402, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [420, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [420, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [407, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [420, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (424,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [452, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [502, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [520, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [520, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [507, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [520, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (524,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [552, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [602, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [620, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [620, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [607, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [620, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (624,224), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [652, 202, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [702, 202, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [720, 220, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [720, 205, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [707, 220, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [720, 220, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (724,224), 7)
  # }}}
  # }}}
  ###  5 ### {{{
  pygame.draw.rect(screen, GREY, [2, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [52, 252, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [70, 270, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 255, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [57, 270, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 270, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (74,274), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [102, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [152, 252, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [170, 270, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 255, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [157, 270, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 270, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (174,274), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [202, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [252, 252, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [270, 270, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 255, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [257, 270, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 270, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (274,274), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [302, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [352, 252, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [370, 270, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 255, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [357, 270, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 270, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (374,274), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [402, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [452, 252, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [470, 270, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 255, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [457, 270, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 270, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (474,274), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [502, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [552, 252, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [570, 270, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 255, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [557, 270, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 270, 25, 10], 0)
  pygame.draw.circle(screen, YELLOW, (574,274), 7)
  # }}}
  pygame.draw.rect(screen, GREY, [602, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [652, 252, 50, 50], 5)
  pygame.draw.rect(screen, GREY, [702, 252, 50, 50], 5)
  # }}}
  ###  6 ### {{{
  pygame.draw.rect   (screen, GREY, [2, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [20, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [20, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [7, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [20, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (24,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [52, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [102, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [120, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [120, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [107, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [120, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (124,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [152, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [202, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [220, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [220, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [207, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [220, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (224,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [252, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [302, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [320, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [320, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [307, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [320, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (324,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [352, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [402, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [420, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [420, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [407, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [420, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (424,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [452, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [502, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [520, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [520, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [507, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [520, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (524,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [552, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [602, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [620, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [620, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [607, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [620, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (624,324), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [652, 302, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [702, 302, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [720, 320, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [720, 305, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [707, 320, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [720, 320, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (724,324), 7)
  # }}}
  # }}}
  ###  7 ### {{{
  pygame.draw.rect   (screen, GREY, [2, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [52, 352, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [70, 370, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 355, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [57, 370, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 370, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (74,374), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [102, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [152, 352, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [170, 370, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 355, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [157, 370, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 370, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (174,374), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [202, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [252, 352, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [270, 370, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 355, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [257, 370, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 370, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (274,374), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [302, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [352, 352, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [370, 370, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 355, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [357, 370, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 370, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (374,374), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [402, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [452, 352, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [470, 370, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 355, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [457, 370, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 370, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (474,374), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [502, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [552, 352, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [570, 370, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 355, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [557, 370, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 370, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (574,374), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [602, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [652, 352, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [702, 352, 50, 50], 5)
  # }}}
  ###  8 ### {{{
  pygame.draw.rect   (screen, GREY, [2, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [20, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [20, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [7, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [20, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (24,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [52, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [102, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [120, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [120, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [107, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [120, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (124,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [152, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [202, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [220, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [220, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [207, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [220, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (224,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [252, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [302, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [320, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [320, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [307, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [320, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (324,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [352, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [402, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [420, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [420, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [407, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [420, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (424,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [452, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [502, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [520, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [520, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [507, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [520, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (524,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [552, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [602, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [620, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [620, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [607, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [620, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (624,424), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [652, 402, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [702, 402, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, PINK, [720, 420, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [720, 405, 10, 25], 0)
  pygame.draw.ellipse(screen, PINK, [707, 420, 20, 10], 0)
  pygame.draw.ellipse(screen, PINK, [720, 420, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (724,424), 7)
  # }}}
  # }}}
  ###  9 ### {{{
  pygame.draw.rect   (screen, GREY, [2, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [52, 452, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [70, 470, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 455, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [57, 470, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [70, 470, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (74,474), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [102, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [152, 452, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [170, 470, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 455, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [157, 470, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [170, 470, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (174,474), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [202, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [252, 452, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [270, 470, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 455, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [257, 470, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [270, 470, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (274,474), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [302, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [352, 452, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [370, 470, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 455, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [357, 470, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [370, 470, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (374,474), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [402, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [452, 452, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [470, 470, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 455, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [457, 470, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [470, 470, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (474,474), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [502, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [552, 452, 50, 50], 5)
  ### Draw Flower {{{
  pygame.draw.ellipse(screen, LBLUE, [570, 470, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 455, 10, 25], 0)
  pygame.draw.ellipse(screen, LBLUE, [557, 470, 20, 10], 0)
  pygame.draw.ellipse(screen, LBLUE, [570, 470, 25, 10], 0)
  pygame.draw.circle (screen, YELLOW, (574,474), 7)
  # }}}
  pygame.draw.rect   (screen, GREY, [602, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [652, 452, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [702, 452, 50, 50], 5)
  # }}}
  ###  9 ### {{{
  pygame.draw.rect   (screen, GREY, [2, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [52, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [102, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [152, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [202, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [252, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [302, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [352, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [402, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [452, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [502, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [552, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [602, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [652, 502, 50, 50], 5)
  pygame.draw.rect   (screen, GREY, [702, 502, 50, 50], 5)
  # }}}
  # }}}
  for bubble in my_bubbles:
    bubble.move(HEIGHT, WIDTH)
    bubble.draw()
  pygame.display.flip()

pygame.quit()

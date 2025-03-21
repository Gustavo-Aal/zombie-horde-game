import pygame
from code.Decorators import singleton
import sys
@singleton
class InputSystem:
  def __init__(self):
    self.key_actions = {}
    self.pressed_key_actions = {}

    self.events = []

  def bind_key(self, key, action):
    self.key_actions[key] = action

  def bind_pressed_key(self, key, action):
    self.pressed_key_actions[key] = action

  def unbind(self, key):
    if key in self.key_actions:
      del self.key_actions[key]

  def handle_event(self):
    self.events = pygame.event.get()
    for event in self.events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()      
      
      if event.type == pygame.KEYDOWN:
        if event.key in self.key_actions:
          self.key_actions[event.key]()
      
    
    pressed_keys = pygame.key.get_pressed()
    for key in self.pressed_key_actions:
      if pressed_keys[key]:
        self.pressed_key_actions[key]() 

      



import pygame
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Const import MENU_OPTIONS
from code.InputSystem import InputSystem
from code.SceneFactory import SceneFactory
from code.Scene import Scene

class Game:
  def __init__(self):
    pygame.init()

    # Game setup
    self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Set window size
    self.scene_factory = SceneFactory(self)                         # Scene factory
    
    self.current_scene: Scene
    self.scene_factory.change_scene("Menu")                         # Start with menu scene
    
    self.input_system = InputSystem()                               # Initialize input system
    
    pygame.display.set_caption("Zombie Horde")                      # Set window caption

  def run(self):    
    clock = pygame.time.Clock()

    while True:
      clock.tick(60)  

      self.current_scene.run()
      self.input_system.handle_event()

      pygame.display.update()

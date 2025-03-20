import pygame.image
import sys
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, COLOR_WHITE, GAME_TITLE, COLOR_TITLE, MENU_OPTIONS
from code.InputSystem import InputSystem
from code.Scene import Scene

class Menu(Scene):

  def __init__(self, window, scene_factory):
    super().__init__(window, scene_factory)

    self.surf = pygame.image.load("./assets/menu.png")
    self.rect = self.surf.get_rect(left=0, top=0)

    self.menu_option = 0
    self.input_system = InputSystem()

    self.input_system.bind_key(pygame.K_UP, self._decrementMenuOption)
    self.input_system.bind_key(pygame.K_DOWN, self._incrementMenuOption)
    self.input_system.bind_key(pygame.K_RETURN, self._selectMenuOption)

    print("Menu initialized")
    
  def run(self):      
      self._renderMenu()   
            
  # private
  def _renderMenu(self):
    # Background
    self.window.blit(source=self.surf, dest=self.rect)
    # Title
    self.bordered_text(text_size=100, text=GAME_TITLE, 
                text_color=(255, 217, 193), 
                text_center_pos=(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 100), 
                border_color=(231, 113, 103), 
                border_thickness=4)
    # Menu options  
    for i in range(len(MENU_OPTIONS)):
      if i == self.menu_option:
        self.menu_text(text_size= 40, text=MENU_OPTIONS[i], text_color=COLOR_TITLE, text_center_pos=(WIN_WIDTH / 2, 300 + 40 * i))
      else: 
        self.menu_text(text_size= 30, text=MENU_OPTIONS[i], text_color=COLOR_WHITE, text_center_pos=(WIN_WIDTH / 2, 300 + 40 * i))



  def _incrementMenuOption(self):
    self.menu_option += 1
    if self.menu_option > len(MENU_OPTIONS) - 1:
      self.menu_option = 0
  
  def _decrementMenuOption(self):
    self.menu_option -= 1
    if self.menu_option < 0:
      self.menu_option = len(MENU_OPTIONS) - 1

  def _selectMenuOption(self):
    match self.menu_option:
      case 0:
        self.scene_factory.change_scene("Level1")
      case 1:
        return "Options"
      case 2:
        return "Exit"
      
      case 4:
        pygame.quit()
        sys.exit()

  def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(source=text_surf, dest=text_rect)

  def bordered_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, border_color: tuple = (0, 0, 0), border_thickness: int = 2):
    offsets = [(-border_thickness, -border_thickness), (-border_thickness, 0), (-border_thickness, border_thickness),
               (0, -border_thickness), (0, border_thickness),
               (border_thickness, -border_thickness), (border_thickness, 0), (border_thickness, border_thickness)]
    
    # Renderiza a borda ao redor do texto
    for dx, dy in offsets:
        self.menu_text(text_size, text, border_color, (text_center_pos[0] + dx, text_center_pos[1] + dy))

    # Renderiza o texto principal por cima
    self.menu_text(text_size, text, text_color, text_center_pos)

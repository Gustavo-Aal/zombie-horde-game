import pygame
from code.Const import COLOR_RED, COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.InputSystem import InputSystem
from code.DbProxy import DbProxy
from code.Scene import Scene
from code.AudioManager import AudioManager

class GameOverMenu(Scene):
  def __init__(self, window: pygame.Surface, score: int, scene_factory):
    super().__init__(window, scene_factory)
    self.score = score
    self.surf = pygame.image.load("./assets/menu.png")
    self.rect = self.surf.get_rect(left=0, top=0)

    self.input_system = InputSystem()
    self.db = DbProxy()
    self.name = ['A', 'A', 'A']
    self.current_char = 0
    
    self.input_system.bind_key(pygame.K_RETURN, self.__save_and_restart)
    self.input_system.bind_key(pygame.K_UP, self.__char_up)
    self.input_system.bind_key(pygame.K_DOWN, self.__char_down)
    self.input_system.bind_key(pygame.K_RIGHT, self.__next_char)
    self.input_system.bind_key(pygame.K_LEFT, self.__prev_char)

    AudioManager.play_music("assets/ambientmain.mp3", force_reload=True)

  def __char_up(self):
    current = ord(self.name[self.current_char])
    if current < ord('Z'):
      self.name[self.current_char] = chr(current + 1)
    else:
      self.name[self.current_char] = 'A'

  def __char_down(self):
    current = ord(self.name[self.current_char])
    if current > ord('A'):
      self.name[self.current_char] = chr(current - 1)
    else:
      self.name[self.current_char] = 'Z'

  def __next_char(self):
    self.current_char = (self.current_char + 1) % 3

  def __prev_char(self):
    self.current_char = (self.current_char - 1) % 3

  def __save_and_restart(self):
    self.db.add_score(''.join(self.name), self.score)
    self.scene_factory.change_scene("Menu")

  def __render_text(self, size: int, text: str, color: tuple, pos: tuple):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    self.window.blit(text_surface, text_rect)

  def run(self):
    self.window.blit(source=self.surf, dest=self.rect)
    overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(180)
    self.window.blit(overlay, (0,0))
    
    self.__render_text(48, "Game Over", COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 40))
    self.__render_text(36, f"Score: {self.score}", COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
    
    name_list = list(self.name)
    self.__render_text(36, "Enter name: ", COLOR_WHITE, (WIN_WIDTH / 2 - 40, WIN_HEIGHT / 2 + 40))
    
    for i, letter in enumerate(name_list):
        color = COLOR_RED if (i == self.current_char and pygame.time.get_ticks() % 1000 < 500) else COLOR_WHITE
        self.__render_text(36, letter, color, (WIN_WIDTH / 2 + 50 + (i * 20), WIN_HEIGHT / 2 + 40))
    
    self.__render_text(36, "Press Enter to save and restart", COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 80))

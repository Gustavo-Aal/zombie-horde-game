from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import *
from code.Player import Player
from code.Scene import Scene
from code.Zombie import Zombie
from code.InputSystem import InputSystem

import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect

class Level(Scene):
  def __init__(self, window, level_name, game_mode, scene_factory):
    super().__init__(window, scene_factory)

    self.level_name = level_name
    self.game_mode = game_mode
    # Background
    self.bg_entity_list: list[Entity] = []
    self.bg_entity_list.extend(EntityFactory.get_entity("Level1Bg"))
    self._scale_bg()

    self.twoPlayers = self.game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]

    # Player
    self.player1 = Player("Player1", (100, WIN_HEIGHT /2))
    if self.twoPlayers:
      self.player2 = Player("Player2", (100, WIN_HEIGHT / 2 + 100))

    self.timeout = 20000


    # Zombies
    self.input_system = InputSystem()
    self.zombies: list[Zombie] = []
    self.max_zombies = 10
    pygame.time.set_timer(EVENT_ZOMBIE, 1000)

    self.frame_count = 0

  def run(self):
    clock = pygame.time.Clock()
    self.frame_count += 1

  
    # Background
    self._draw_bg()
    
    # Player
    self.player1.run(self.window, self.frame_count)
    if self.twoPlayers:
      self.player2.run(self.window, self.frame_count)

    # Zombie
    for event in self.input_system.events:
      if event.type == EVENT_ZOMBIE:
        self.zombies.append(EntityFactory.get_entity("Zombie"))

    for zombie in self.zombies:
      zombie.run(self.window, self.frame_count)

    # HUD
    self._draw_hud(clock)

    

  def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(topleft=text_pos)
    self.window.blit(source=text_surf, dest=text_rect)


  def _scale_bg(self):
    for entity in self.bg_entity_list:
      scale = 600 / entity.surf.get_height()
      new_width = int(entity.surf.get_width() * scale)
      entity.surf = pygame.transform.scale(entity.surf, (new_width, 600))        
      entity.rect = entity.surf.get_rect(left=entity.rect.left, top=entity.rect.top)

  def _draw_bg(self):
    for entity in self.bg_entity_list:
      self.window.blit(entity.surf, entity.rect)
      entity.move()

  def _draw_hud(self, clock):
    self.level_text(24, f"{self.level_name} - Timeout: {self.timeout / 1000 :.1f}s", COLOR_WHITE, (24,5))
    self.level_text(24, f"fps {clock.get_fps() :.0f}", COLOR_WHITE, (24, WIN_HEIGHT - 35))
    self.level_text(24, f"entidades {len(self.bg_entity_list)}", COLOR_WHITE, (24, WIN_HEIGHT - 20))
    self.level_text(24, f"zombies {len(self.zombies)}", COLOR_WHITE, (24, WIN_HEIGHT - 40))

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE
from code.Player import Player
from code.Scene import Scene

import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect

class Level(Scene):
  def __init__(self, window, level_name, game_mode, scene_factory):
    super().__init__(window, scene_factory)

    self.level_name = level_name
    self.game_mode = game_mode
    self.entity_list: list[Entity] = []
    self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))


    self.player = Player("Player", (100, WIN_HEIGHT /2))

    self.timeout = 20000

    self.frame_count = 0

  def run(self):
    clock = pygame.time.Clock()
    
    self.frame_count += 1

    # Background parallax
    for entity in self.entity_list:
      scale = 600 / entity.surf.get_height()
      new_width = int(entity.surf.get_width() * scale)
      entity.surf = pygame.transform.scale(entity.surf, (new_width, 600))        
      entity.rect = entity.surf.get_rect(left=entity.rect.left, top=entity.rect.top)
      self.window.blit(entity.surf, entity.rect)
      entity.move()
      
    # HUD
    self.level_text(24, f"{self.level_name} - Timeout: {self.timeout / 1000 :.1f}s", COLOR_WHITE, (24,5))
    self.level_text(24, f"fps {clock.get_fps() :.0f}", COLOR_WHITE, (24, WIN_HEIGHT - 35))
    self.level_text(24, f"entidades {len(self.entity_list)}", COLOR_WHITE, (24, WIN_HEIGHT - 20))

    self.player.run(self.window, self.frame_count)

  def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(topleft=text_pos)
    self.window.blit(source=text_surf, dest=text_rect)


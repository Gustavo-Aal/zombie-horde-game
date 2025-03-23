from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.EntityFactory import EntityFactory
from code.Const import *
from code.Player import Player
from code.Scene import Scene
from code.Zombie import Zombie
from code.InputSystem import InputSystem
from code.AudioManager import AudioManager

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
    self.__scale_bg()

    # Player
    self.player = Player("Player", (100, WIN_HEIGHT /2))

    self.timeout = 20000
    self.clock = pygame.time.Clock()  # Create clock once here

    # Zombies
    self.input_system = InputSystem()
    self.zombies: list[Zombie] = []
    self.max_zombies = 10
    pygame.time.set_timer(EVENT_ZOMBIE, 1000)

    self.frame_count = 0

    AudioManager.play_music("assets/battletheme.mp3", force_reload=True)
    pygame.mixer_music.set_volume(0.25)

  def run(self):
    self.clock.tick(60) 
    self.frame_count += 1
    
    self.timeout -= self.clock.get_time()  
    
    if self.player.health > 0 and self.timeout > 0:
      # Background
      self.__draw_bg()
      
      # Player 1
      self.player.run(self.window, self.frame_count)
      for shot in self.player.player_shots:
        shot.run(self.window, self.frame_count)

      # Zombie
      for event in self.input_system.events:
        if event.type == EVENT_ZOMBIE:  
          self.zombies.append(EntityFactory.get_entity("Zombie"))

      for zombie in self.zombies:
        zombie.run(self.window, self.frame_count)

      EntityMediator.verify_collision([self.player] + self.zombies, self.player)
      EntityMediator.verify_health(self.zombies)

      # HUD
      self.__draw_hud(self.clock)
    else:
      self.__game_over()

  def __level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(topleft=text_pos)
    self.window.blit(source=text_surf, dest=text_rect)

  def __scale_bg(self):
    for entity in self.bg_entity_list:
      scale = 600 / entity.surf.get_height()
      new_width = int(entity.surf.get_width() * scale)
      entity.surf = pygame.transform.scale(entity.surf, (new_width, 600))        
      entity.rect = entity.surf.get_rect(left=entity.rect.left, top=entity.rect.top)

  def __draw_bg(self):
    for entity in self.bg_entity_list:
      self.window.blit(entity.surf, entity.rect)
      entity.move()

  def __draw_hud(self, clock):
    self.__level_text(36, f"Health: {self.player.health}", COLOR_RED, (24, 8))
    self.__level_text(36, f"Score: {self.player.score}", COLOR_WHITE, (24, 40))

    self.__level_text(36, f"Zombies {len(self.zombies)}", COLOR_WHITE, (24, WIN_HEIGHT - 60))
    self.__level_text(36, f"{self.level_name} - Timeout: {self.timeout / 1000 :.1f}s", COLOR_WHITE, (24, WIN_HEIGHT - 35))
  def __game_over(self):
    self.scene_factory.change_scene("GameOverMenu", score= self.player.score)


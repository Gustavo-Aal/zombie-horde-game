import pygame
from code.Const import PLAYER_SHOT_SPEED
from code.Entity import Entity

class PlayerShot(Entity):
  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

    self.speed = PLAYER_SHOT_SPEED

    scale = 0.025
    self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * scale), int(self.surf.get_height() * scale)))
    self.rect = self.surf.get_rect(center=position)

  def move(self):
    self.rect.centerx += self.speed

  def run(self, window: pygame.Surface, frame_count: int):
    window.blit(self.surf, self.rect)
    self.move()

  def take_damage(self, damage: int):
    pass

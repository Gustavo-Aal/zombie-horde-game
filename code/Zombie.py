import pygame
from code.Entity import Entity
from code.Const import ZOMBIE_SPEED, WIN_WIDTH
class Zombie(Entity):
  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

    
    scale = 0.5
    self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * scale), int(self.surf.get_height() * scale)))
    self.rect = self.surf.get_rect(center=position)

    self.speed = ZOMBIE_SPEED

  def move(self, ):
    self.rect.centerx -= self.speed

    if self.rect.right <= 0:
      self.rect.left = WIN_WIDTH

  def run(self, window: pygame.Surface, frame_count: int):
    self.move()
    window.blit(self.surf, self.rect)



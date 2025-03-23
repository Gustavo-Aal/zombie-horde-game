import pygame
from code.Entity import Entity
from code.Const import ZOMBIE_SPEED, WIN_WIDTH
import random
class Zombie(Entity):
  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

    
    scale = 0.5
    

    self.zombie_sprites = []
    for i in range(17):
      sprite = pygame.image.load(f"./assets/zombie_move_{i}.png").convert_alpha()
      sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
      self.zombie_sprites.append(sprite)
    
    self.surf = self.zombie_sprites[random.randint(0, 16)]
    self.rect = self.surf.get_rect(center=position)
    self.rect = pygame.Rect(
      self.rect.left,
      self.rect.top,
      self.rect.width - 50,
      self.rect.height - 50
    )
    
                           

    self.speed = ZOMBIE_SPEED

  def move(self, ):
    self.rect.centerx -= self.speed
  def run(self, window: pygame.Surface, frame_count: int):
    self.move()
    window.blit(self.zombie_sprites[(frame_count // 4) % 17], (self.rect.left - 25, self.rect.top - 15))
    
  def take_damage(self, dealer, damage: int):
    self.health -= damage
    if self.health <= 0:
      self.health = 0

    if dealer.name == "Player":
      dealer.score += 1


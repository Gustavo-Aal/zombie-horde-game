from code.Entity import Entity
from code.InputSystem import InputSystem
import pygame
from code.Const import WIN_HEIGHT

class Player(Entity):
  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

    scale = 0.5
    self.surf = pygame.image.load("./assets/player.png").convert_alpha()
    self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * scale), int(self.surf.get_height() * scale)))
    self.rect = self.surf.get_rect(center=position)

    self.input_system = InputSystem()
    self.input_system.bind_pressed_key(pygame.K_UP, lambda: self.move(-5))
    self.input_system.bind_pressed_key(pygame.K_DOWN, lambda: self.move(5))

    self.feet_sprites = []

    for i in range(20):

      sprite = pygame.image.load(f"./assets/survivor-run_{i}.png").convert_alpha()
      sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
      self.feet_sprites.append(sprite)
    
    self.feet_rect = self.feet_sprites[0].get_rect(center=(self.rect.centerx - 30, self.rect.centery + 10))

  def move(self, value: int):
    self.rect.centery += value
    self.feet_rect.centery = self.rect.centery + 10
  
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > WIN_HEIGHT:
      self.rect.bottom = WIN_HEIGHT

  def run(self, window: pygame.Surface, frame_count: int):
    window.blit(self.feet_sprites[(frame_count // 2) % 20], self.feet_rect)
    window.blit(self.surf, self.rect)
from code.Entity import Entity
from code.InputSystem import InputSystem
from code.Const import *
from code.PlayerShot import PlayerShot
from code.AudioManager import AudioManager
import pygame
import random

class Player(Entity):
  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

    scale = 0.5
    self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * scale), int(self.surf.get_height() * scale)))
    self.rect = self.surf.get_rect(center=position)

    self.speed = PLAYER_SPEED

    self.input_system = InputSystem()
    self.__setup_input()

    self.player_shots = []
    self.shot_cooldown = PLAYER_SHOT_COOLDOWN
    self.next_time_to_shoot = 0
    self.score = 0

    self.feet_sprites = []

    for i in range(20):
      sprite = pygame.image.load(f"./assets/survivor-run_{i}.png").convert_alpha()
      sprite = pygame.transform.scale(sprite, (int(sprite.get_width() * scale), int(sprite.get_height() * scale)))
      self.feet_sprites.append(sprite)
    
    self.feet_rect = self.feet_sprites[0].get_rect(center=(self.rect.centerx - 30, self.rect.centery + 10))

  def move(self, vector: tuple[int, int]):
    # Move player
    self.rect.centerx += vector[0]
    self.rect.centery += vector[1]
    self.feet_rect.centerx = self.rect.centerx - 30
    self.feet_rect.centery = self.rect.centery + 10

    # Check boundaries
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > WIN_HEIGHT:
      self.rect.bottom = WIN_HEIGHT
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > WIN_WIDTH:
      self.rect.right = WIN_WIDTH

  def run(self, window: pygame.Surface, frame_count: int):
    window.blit(self.feet_sprites[(frame_count // 4) % 20], self.feet_rect)
    window.blit(self.surf, self.rect)


  def shoot(self):
    time = pygame.time.get_ticks()
    if time > self.next_time_to_shoot: 
      audio_path = f"assets/rifleshot{random.randint(0, 2)}.wav"
      AudioManager.play_sound(audio_path)

      self.next_time_to_shoot = time + self.shot_cooldown
      self.player_shots.append(PlayerShot("PlayerShot", (self.rect.right + 15, self.rect.bottom - 18)))

  def __setup_input(self):
    self.input_system.bind_pressed_key(PLAYER_KEY_UP, lambda: self.move((0, -self.speed)))
    self.input_system.bind_pressed_key(PLAYER_KEY_DOWN, lambda: self.move((0, self.speed)))
    self.input_system.bind_pressed_key(PLAYER_KEY_LEFT, lambda: self.move((-self.speed, 0)))
    self.input_system.bind_pressed_key(PLAYER_KEY_RIGHT, lambda: self.move((self.speed, 0)))
    self.input_system.bind_pressed_key(PLAYER_KEY_SHOOT, self.shoot)

  def reload(self):
    self.ammo = PLAYER_MAX_AMMO

  def take_damage(self, damage: int):
    self.health -= damage
    if self.health <= 0:
      self.health = 0



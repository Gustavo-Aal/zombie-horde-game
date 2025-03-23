from abc import ABC
import pygame
import random
class AudioManager(ABC):
    
  def play_music(path: str, force_reload: bool = False):

    if not pygame.mixer_music.get_busy() or force_reload:
      pygame.mixer_music.load(path)
      pygame.mixer_music.play(-1)

  def play_sound(path: str):
    sound = pygame.mixer.Sound(path)
    sound.set_volume(0.1)
    sound.play()

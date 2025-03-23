from typing import List
from code.Entity import Entity
from code.Zombie import Zombie  
from code.Const import ZOMBIE_DAMAGE, PLAYER_SHOT_DAMAGE

class EntityMediator:
  
  @staticmethod
  def __verify_collision_window(entity: Entity):
    # Metodo muito ruim
    if isinstance(entity, Zombie):
      if entity.rect.right <= 0:
        entity.health = 0

  def verify_collision(entity_list: List[Entity], player):
    for entity in entity_list:
      EntityMediator.__verify_collision_window(entity)
      
      # Check if entity is a zombie
      if isinstance(entity, Zombie):
        # Check collision with player
        if entity.rect.colliderect(player.rect):
          player.health -= ZOMBIE_DAMAGE
          # entity.health = 0    # Remove zombie after hit
        
        # Check collision with player shots
        for shot in player.player_shots:
          if entity.rect.colliderect(shot.rect):
            entity.take_damage(player, PLAYER_SHOT_DAMAGE)
            player.player_shots.remove(shot)

  @staticmethod
  def verify_health(entity_list: List[Entity]):
    for entity in entity_list:
      if entity.health <= 0:
        entity_list.remove(entity)


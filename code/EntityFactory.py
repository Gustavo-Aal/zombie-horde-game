from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Zombie import Zombie
import random

class EntityFactory:
 
  @staticmethod
  def get_entity(entity_name: str, position: tuple = (0,0)):
    match entity_name:
      case 'Level1Bg':
        list_bg = []

        for i in range(1): # Quantidade de backgrounds
          list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
          list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))

        return list_bg

      case 'Player1':
        return Player("Player", (10, WIN_HEIGHT/2))

      case 'Zombie':
        return Zombie("Zombie", (WIN_WIDTH, random.randint(25, WIN_HEIGHT -25)))


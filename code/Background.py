from code.Entity import Entity
from code.Const import WIN_WIDTH, BACKGROUND_SPEED
class Background(Entity):
  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

  def move(self, ):
    self.rect.centerx -= BACKGROUND_SPEED

    if self.rect.right <= 0:
      self.rect.left = WIN_WIDTH

  def take_damage(self, damage: int):
    pass

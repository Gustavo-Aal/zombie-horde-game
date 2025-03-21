from code.Menu import Menu
from code.Level import Level
from code.Decorators import singleton 
from code.Const import MENU_OPTIONS

@singleton
class SceneFactory:
  def __init__(self, game):
    self.game = game


  def change_scene(self, scene_name):
    match scene_name:
      case "Menu":
        self.game.current_scene = Menu(self.game.window, self)
      case "Level1":
        self.game.current_scene = Level(self.game.window, "Level1", MENU_OPTIONS[0], self)


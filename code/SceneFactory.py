from code.Menu import Menu
from code.Level import Level
from code.GameOverMenu import GameOverMenu
from code.Scores import Scores
from code.Decorators import singleton 
from code.Const import MENU_OPTIONS
from code.InputSystem import InputSystem

@singleton
class SceneFactory:
  def __init__(self, game):
    self.game = game
    self.input_system = InputSystem()

  def change_scene(self, scene_name, score=None):

    self.input_system.clear_binds()

    match scene_name:
      case "Menu":
        self.game.current_scene = Menu(self.game.window, self)
      case "Level1":
        self.game.current_scene = Level(self.game.window, "Level1", MENU_OPTIONS[0], self)
      case "Scores":
        self.game.current_scene = Scores(self.game.window, self)

      case "GameOverMenu":
        self.game.current_scene = GameOverMenu(self.game.window, score, self)


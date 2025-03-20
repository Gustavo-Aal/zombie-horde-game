from code.InputSystem import InputSystem

class Scene:
  def __init__(self, window, scene_factory):
    self.window = window
    self.input_system = InputSystem()
    self.scene_factory = scene_factory

  def run(self):
    pass


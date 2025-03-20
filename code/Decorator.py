def meu_decorator(func):
  def wrapper():
    print("Algo antes da função")
    func()
    print("Algo depois da função")
  return wrapper
  

@meu_decorator
def hello_world():
  print("Hello, world!")




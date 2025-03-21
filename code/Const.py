import pygame

# B
BACKGROUND_SPEED = 2

# C
COLOR_ORANGE = (255, 75, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_TITLE = (231, 113, 103)

# E
EVENT_ZOMBIE = pygame.USEREVENT + 1

# G

GAME_TITLE = "Zombie Horde"

# M
MENU_OPTIONS = (
  "New Game",
  "New Game 2P - Cooperative",
  "New Game 2P - Competitive",
  "Score",
  "Exit"
)

# P
PLAYER_KEY_UP = {
  "Player1": pygame.K_UP,
  "Player2": pygame.K_w
}
PLAYER_KEY_DOWN = {
  "Player1": pygame.K_DOWN,
  "Player2": pygame.K_s
}
PLAYER_KEY_LEFT = {
  "Player1": pygame.K_LEFT,
  "Player2": pygame.K_a
}
PLAYER_KEY_RIGHT = {
  "Player1": pygame.K_RIGHT,
  "Player2": pygame.K_d
} 

PLAYER_SPEED = 5
ZOMBIE_SPEED = 3






# W
WIN_WIDTH = 1000
WIN_HEIGHT = 600


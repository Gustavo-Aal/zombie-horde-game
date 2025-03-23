import pygame
from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Scene import Scene
from code.DbProxy import DbProxy

class Scores(Scene):
    def __init__(self, window: pygame.Surface, scene_factory):
        super().__init__(window, scene_factory)
        self.db = DbProxy()
        self.surf = pygame.image.load("./assets/menu.png")
        self.rect = self.surf.get_rect(left=0, top=0)
        
        self.input_system.bind_key(pygame.K_RETURN, self.__return_to_menu)

    def __return_to_menu(self):
        self.scene_factory.change_scene("Menu")

    def __render_text(self, size: int, text: str, color: tuple, pos: tuple):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        self.window.blit(text_surface, text_rect)

    def run(self):
        self.window.blit(source=self.surf, dest=self.rect)
        
        overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        self.window.blit(overlay, (0,0))
        
        scores = self.db.get_top_scores()
        
        self.__render_text(40, "High Scores", COLOR_WHITE, (WIN_WIDTH/2, 50))
        
        y_pos = 120
        for i, (name, score) in enumerate(scores[:10], 1):  
            self.__render_text(36, f"{i}. {name}: {score}", COLOR_WHITE, (WIN_WIDTH/2, y_pos))
            y_pos += 40
            
        self.__render_text(36, "Press Enter to return to menu", COLOR_WHITE, (WIN_WIDTH/2, WIN_HEIGHT - 40))
